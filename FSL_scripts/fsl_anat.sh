#
# https://web.mit.edu/fsl_v5.0.10/fsl/doc/wiki/fsl_anat.html
#


# set up FSL environment variables
export FSLOUTPUTTYPE=NIFTI
export FSLDIR=/home/jjiang10/fsl

export MNI_DIR=/data/imaging_nas/MNI

cd /data/imaging_nas/NACC/MRI/test_run/1.3.12.2.1107.5.2.19.45135.30000019102413580947700000004/1.3.12.2.1107.5.2.19.45135.2019102410105747588520627.0.0.0/

# 
cd /data/imaging_nas/NACC/MRI/test_run
unzip NACC999566_128401136196408191922470400351783935291545466831236476ni.zip -d NACC999566_128401136196408191922470400351783935291545466831236476 

# run with single thread to avoid potential issues with parallel processing in cluster environment
unset SGE_ROOT
unset SLURM_JOB_ID
export FSLPARALLEL=0
# run fsl_anat to process the brain MRI image (an example)
${FSLDIR}/bin/fsl_anat -i 1.3.12.2.1107.5.2.19.45135.2019102410105747588520627.0.0.0.nii -o /data/imaging_nas/NACC/MRI/test_run_output/ --clobber

# run fsl_anat on all the example images in the test_run folder
mkdir /data/imaging_nas/NACC/MRI/test_run_output_all
for subdir in /data/imaging_nas/NACC/MRI/test_run/*/; do
    echo "Processing subject in $subdir"
    nifti_file=$(find "$subdir" -name "*.nii" | head -n 1)
    if [ -n "$nifti_file" ]; then
        output_dir="/data/imaging_nas/NACC/MRI/test_run_output_all/$(basename "$subdir")"
        ${FSLDIR}/bin/fsl_anat -i "$nifti_file" -o "$output_dir" --clobber
    else
        echo "No NIfTI file found in $subdir"
    fi
done



# folder structure of fsl_anat output:
# sub-001/
#   .anat/...
#   first/...
# sub-002/
#   .anat/...
#   first/...

python first_idp_extract.py --root /Volumes/bai/NACC/MRI/test_run_output_all/ --out /Volumes/bai/NACC/MRI/test_run_output_all/first_features.csv --label-lut /Volumes/bai/NACC/MRI/first_all_fast_lut.txt

 python first_idp_extract.py --subjects-glob /Volumes/bai/NACC/MRI/test_run_output --out /Volumes/bai/NACC/MRI/test_run_output/first_features.csv

