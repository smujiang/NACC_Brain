import pyvista as pv
import glob
import os

import platform

os_name = platform.system()

if os_name == "Darwin":
    vtk_dir = "/Volumes/bai/NACC/MRI/test_run_output_all"
else:
    vtk_dir = "/data/imaging_nas/NACC/MRI/test_run_output_all"

output_dir = os.path.join(os.path.expanduser("~"),"Downloads", "gifs")
# output_dir = os.path.join(vtk_dir, "gifs")
os.makedirs(output_dir, exist_ok=True)

case_serial_number_list = ["1.2.840.113619.6.408.191922470400351783935291545466831236476",
                           "1.2.840.113619.6.410.144173852630529424350093756054799406936",
                            "1.3.12.2.1107.5.2.19.45135.30000014111016033540100000958",
                            "1.3.12.2.1107.5.2.19.45135.30000019102413580947700000004"]

case_NACC_mapping = {
    "1.2.840.113619.6.408.191922470400351783935291545466831236476": "NACC999566_1",
    "1.2.840.113619.6.410.144173852630529424350093756054799406936": "NACC999566_2",
    "1.3.12.2.1107.5.2.19.45135.30000014111016033540100000958": "NACC999546_1",
    "1.3.12.2.1107.5.2.19.45135.30000019102413580947700000004": "NACC999546_2"
}

for case_serial_number in case_serial_number_list:
    case_folder = os.path.join(vtk_dir, case_serial_number+".anat", "first_results")
    print(f"Processing case {case_serial_number} in folder {case_folder}...")
    vtk_files = glob.glob(os.path.join(case_folder, "*_first.vtk"))
    print(f"Case {case_serial_number}: Found {len(vtk_files)} vtk files.")
    plotter = pv.Plotter(window_size=(1000, 800))

    structure_colors = {
        "Hipp": "red",
        "Amyg": "yellow",
        "Caud": "blue",
        "Puta": "green",
        "Pall": "purple",
        "Thal": "cyan",
        "Accu": "orange",
        "BrStem": "brown"
    }

    plotter = pv.Plotter()

    for vtk_file in vtk_files:
        
        mesh = pv.read(vtk_file)
        
        name = os.path.basename(vtk_file)
        
        color = "gray"
        for key in structure_colors:
            if key in name:
                color = structure_colors[key]
        
        plotter.add_mesh(mesh, color=color, smooth_shading=True)

    plotter.add_legend([
        ("Hippocampus", "red"),
        ("Amygdala", "yellow"),
        ("Caudate", "blue"),
        ("Putamen", "green"),
        ("Pallidum", "purple"),
        ("Thalamus", "cyan"),
        ("Accumbens", "orange"),
        ("Brainstem", "brown")
    ])


    # open gif file

    save_gif_fn = os.path.join(output_dir, case_NACC_mapping[case_serial_number]+"_brain_structures.gif")
    plotter.open_gif(save_gif_fn)

    # set camera
    plotter.view_isometric()

    # rotate and save frames
    n_frames = 60

    for i in range(n_frames):
        
        # plotter.camera.azimuth(360 / n_frames)
        plotter.camera.Azimuth(360 / n_frames)
        
        plotter.render()
        
        plotter.write_frame()

    # close
    plotter.close()


