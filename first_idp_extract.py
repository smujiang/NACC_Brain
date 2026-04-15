
#!/usr/bin/env python3
"""
Extract FSL FIRST-derived features per subject:
- Label volumes from *_all_fast_firstseg.nii.gz (robust, using NIfTI voxel volume)
- Mesh surface area + mesh volume from *_first.vtk
- Shape mode summaries from *_first.bvars
Outputs one row per subject to CSV.

Dependencies:
  pip install numpy pandas nibabel pyvista
Optional (recommended for speed/robust):
  pip install vtk  # pyvista pulls vtk in many setups anyway

Usage examples:
  # 1) Root contains subfolders per subject:
  python first_idp_extract.py --root /data/first_outputs --out first_features.csv

  # 2) If subject folders follow a pattern:
  python first_idp_extract.py --subjects-glob "/data/first_outputs/sub-*/ses-*" --out first_features.csv

  # 3) If your FIRST seg file has a nonstandard name:
  python first_idp_extract.py --root /data --seg-glob "*_fast_firstseg.nii.gz" --out out.csv

  # 4) Provide a label LUT (CSV: label,name) to name label-volume columns:
  python first_idp_extract.py --root /data --label-lut label_lut.csv --out out.csv
"""

from __future__ import annotations

import argparse
import glob
import json
import os
from pathlib import Path
from typing import Dict, List, Optional, Tuple

import numpy as np
import pandas as pd
import nibabel as nib

# pyvista can be a bit noisy in headless envs; keep it simple
import pyvista as pv


def load_label_lut(path: str) -> Dict[int, str]:
    """
    Load label lookup table.
    Supported:
      - CSV with columns: label,name
      - JSON dict: {"10": "Left-Hippocampus", ...} or {10: "..."}
    """
    p = Path(path)
    if not p.exists():
        raise FileNotFoundError(f"Label LUT not found: {path}")

    if p.suffix.lower() == ".json":
        d = json.loads(p.read_text())
        out = {}
        for k, v in d.items():
            out[int(k)] = str(v)
        return out

    # assume CSV/TSV
    df = pd.read_csv(p)
    if "label" not in df.columns or "name" not in df.columns:
        raise ValueError("Label LUT CSV must have columns: label,name")
    return {int(r["label"]): str(r["name"]) for _, r in df.iterrows()}


def nifti_voxel_volume_mm3(img: nib.Nifti1Image) -> float:
    # robust voxel dimensions (mm)
    zooms = img.header.get_zooms()[:3]
    return float(zooms[0] * zooms[1] * zooms[2])


def extract_label_volumes(seg_path: str,
                          label_lut: Optional[Dict[int, str]] = None,
                          exclude_zero: bool = True) -> Dict[str, float]:
    """
    Compute volume (mm^3) per label from FIRST segmentation labelmap.
    Robustness:
      - Uses NIfTI voxel volume from header
      - Uses unique labels present (no assumptions about label IDs)
    """
    img = nib.load(seg_path)
    data = img.get_fdata(dtype=np.float32)  # labels are ints but stored in float sometimes
    voxel_vol = nifti_voxel_volume_mm3(img)

    labels = np.unique(data.astype(np.int32))
    if exclude_zero:
        labels = labels[labels != 0]

    feats: Dict[str, float] = {}
    feats["seg_voxel_volume_mm3"] = voxel_vol

    for lab in labels:
        count = int(np.sum(data == lab))
        vol = count * voxel_vol
        if label_lut and int(lab) in label_lut:
            name = label_lut[int(lab)]
            # safe column name
            col = f"seg_labelvol_{name}_mm3"
        else:
            col = f"seg_labelvol_label{int(lab)}_mm3"
        feats[col] = float(vol)

    # total labeled volume (sum of nonzero labels)
    total_count = int(np.sum(data != 0)) if exclude_zero else int(data.size)
    feats["seg_total_labeled_volume_mm3"] = float(total_count * voxel_vol)

    return feats


def infer_structure_key_from_filename(vtk_path: str) -> str:
    """
    Create a stable "structure key" from FIRST vtk filename.
    Examples:
      T1_first-L_Hipp_first.vtk -> L_Hipp
      T1_first-R_Amyg_first.vtk -> R_Amyg
      L_Hipp_first.vtk          -> L_Hipp
    """
    base = Path(vtk_path).name

    # strip extension
    stem = base[:-4] if base.lower().endswith(".vtk") else Path(vtk_path).stem

    # common patterns include "...-L_Hipp_first" or "L_Hipp_first"
    # take the last token after '-' if present
    if "-" in stem:
        tail = stem.split("-")[-1]
    else:
        tail = stem

    # remove trailing "_first" if present
    if tail.endswith("_first"):
        tail = tail[:-len("_first")]

    return tail


def mesh_features(vtk_path: str) -> Dict[str, float]:
    """
    Compute mesh surface area + volume from vtk PolyData.
    Notes:
      - Volume is only meaningful for CLOSED surfaces; FIRST structures usually are.
      - If mesh is not closed, volume may be 0 or unreliable.
    """
    mesh = pv.read(vtk_path)

    # surface area
    area = float(mesh.area)

    # volume: pyvista uses VTK mass properties; should work on closed polydata
    # If not closed, this can be 0 or nonsense; we’ll still report it.
    vol = float(mesh.volume)

    # basic vertex/face counts (often useful)
    n_points = int(mesh.n_points)
    n_cells = int(mesh.n_cells)

    return {
        "mesh_surface_area_mm2": area,
        "mesh_volume_mm3": vol,
        "mesh_n_points": float(n_points),
        "mesh_n_faces": float(n_cells),
    }


def bvars_summaries(bvars_path: str, n_modes: int = 20) -> Dict[str, float]:
    """
    Read FIRST .bvars and compute per-mode summaries.
    bvars: [n_vertices, n_modes_total]
    We output for first n_modes:
      - mean
      - std
      - mean_abs
      - rms
    """
    arr = np.loadtxt(bvars_path)
    if arr.ndim == 1:
        # edge case: single mode file
        arr = arr[:, None]

    n_total = arr.shape[1]
    use = min(n_modes, n_total)

    feats: Dict[str, float] = {
        "bvars_n_vertices": float(arr.shape[0]),
        "bvars_n_modes_total": float(n_total),
    }

    for m in range(use):
        v = arr[:, m]
        feats[f"bvars_mode{m+1:02d}_mean"] = float(np.mean(v))
        feats[f"bvars_mode{m+1:02d}_std"] = float(np.std(v, ddof=1) if v.size > 1 else 0.0)
        feats[f"bvars_mode{m+1:02d}_mean_abs"] = float(np.mean(np.abs(v)))
        feats[f"bvars_mode{m+1:02d}_rms"] = float(np.sqrt(np.mean(v**2)))

    return feats


def find_one(patterns: List[str], folder: str) -> Optional[str]:
    for pat in patterns:
        hits = sorted(glob.glob(os.path.join(folder, pat)))
        if hits:
            return hits[0]
    return None


def collect_subject_features(subject_dir: str,
                             seg_glob: str,
                             vtk_glob: str,
                             bvars_glob: str,
                             label_lut: Optional[Dict[int, str]],
                             bvars_modes: int) -> Dict[str, float]:
    """
    Extract all features for a single subject directory.
    """
    feats: Dict[str, float] = {}
    feats["subject_dir"] = subject_dir

    # --- segmentation label volumes ---
    seg_path = find_one([seg_glob], subject_dir)
    if seg_path:
        feats.update(extract_label_volumes(seg_path, label_lut=label_lut))
        feats["firstseg_path"] = seg_path
    else:
        feats["firstseg_path"] = ""
        feats["warning_missing_firstseg"] = 1.0

    # --- meshes + bvars ---
    vtk_files = sorted(glob.glob(os.path.join(subject_dir, vtk_glob)))
    feats["n_vtk_files"] = float(len(vtk_files))

    for vtk_path in vtk_files:
        struct = infer_structure_key_from_filename(vtk_path)

        # mesh features
        mf = mesh_features(vtk_path)
        for k, v in mf.items():
            feats[f"{struct}_{k}"] = v

        # match bvars (same stem, .bvars)
        bvars_path = Path(vtk_path).with_suffix(".bvars")
        if not bvars_path.exists():
            # try glob fallback if naming differs
            # e.g., "T1_first-L_Hipp_first.bvars" should match
            candidates = glob.glob(os.path.join(subject_dir, bvars_glob))
            # best-effort match by structure string
            match = [c for c in candidates if struct in Path(c).name]
            bvars_path = Path(match[0]) if match else bvars_path

        if bvars_path.exists():
            bf = bvars_summaries(str(bvars_path), n_modes=bvars_modes)
            for k, v in bf.items():
                feats[f"{struct}_{k}"] = v
        else:
            feats[f"{struct}_warning_missing_bvars"] = 1.0

    return feats


def list_subject_dirs(args) -> List[str]:
    if args.subjects_glob:
        dirs = sorted([p for p in glob.glob(args.subjects_glob) if os.path.isdir(p)])
        return dirs
    # default: immediate subfolders of root
    root = Path(args.root)
    dirs = sorted([str(p) for p in root.iterdir() if p.is_dir()])
    return dirs


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", type=str, default=".", help="Root directory containing subject folders.")
    ap.add_argument("--subjects-glob", type=str, default="", help="Optional glob to enumerate subject folders.")
    ap.add_argument("--out", type=str, required=True, help="Output CSV path.")
    ap.add_argument("--seg-glob", type=str, default="*all_fast_firstseg*.nii*",
                    help="Glob within subject folder for FIRST segmentation labelmap.")
    ap.add_argument("--vtk-glob", type=str, default="*_first.vtk", help="Glob within subject folder for FIRST vtk meshes.")
    ap.add_argument("--bvars-glob", type=str, default="*.bvars", help="Glob within subject folder for bvars.")
    ap.add_argument("--label-lut", type=str, default="", help="Optional label LUT (CSV label,name or JSON dict).")
    ap.add_argument("--bvars-modes", type=int, default=20, help="How many bvars modes to summarize (first N).")
    args = ap.parse_args()

    label_lut = load_label_lut(args.label_lut) if args.label_lut else None
    print(f"[INFO] Using label LUT with {len(label_lut) if label_lut else 0} entries.")
    subject_dirs = list_subject_dirs(args)
    if not subject_dirs:
        raise RuntimeError("No subject directories found. Check --root or --subjects-glob.")
    print(f"[INFO] Found {len(subject_dirs)} subject directories.")
    rows = []
    for sd in subject_dirs:
        try:
            row = collect_subject_features(
                subject_dir=sd,
                seg_glob=args.seg_glob,
                vtk_glob=args.vtk_glob,
                bvars_glob=args.bvars_glob,
                label_lut=label_lut,
                bvars_modes=args.bvars_modes
            )
        except Exception as e:
            row = {"subject_dir": sd, "error": str(e)}
        rows.append(row)

    df = pd.DataFrame(rows)

    # Move key columns to front if present
    front = [c for c in ["subject_dir", "firstseg_path", "n_vtk_files", "seg_voxel_volume_mm3", "seg_total_labeled_volume_mm3", "error"] if c in df.columns]
    rest = [c for c in df.columns if c not in front]
    df = df[front + rest]

    df.to_csv(args.out, index=False)
    print(f"[OK] Wrote: {args.out}")
    print(f"[OK] Subjects: {len(df)}")
    print("[TIP] If you want named label volumes, pass --label-lut label_lut.csv")


if __name__ == "__main__":
    main()

