cd /data/imaging_nas/NACC/MRI

# create example images folder:
mkdir test_run

cp all/nifti/NACCNACC998282_131221107524316709230000020092114243015000000001ni.zip test_run/
cp all/nifti/NACC999546_13122110752194513530000014111016033540100000958ni.zip test_run/
cp all/nifti/NACC999546_13122110752194513530000019102413580947700000004ni.zip test_run/
cp all/nifti/NACC999566_128401136196408191922470400351783935291545466831236476ni.zip test_run/

unzip test_run/NACCNACC998282_131221107524316709230000020092114243015000000001ni.zip -d test_run/
unzip test_run/NACC999546_13122110752194513530000014111016033540100000958ni.zip -d test_run/
unzip test_run/NACC999546_13122110752194513530000019102413580947700000004ni.zip -d test_run/
unzip test_run/NACC999566_128401136196408191922470400351783935291545466831236476ni.zip -d test_run/


# set up FSL environment variables
export FSLOUTPUTTYPE=NIFTI
export FSLDIR=/home/jjiang10/fsl

export MNI_DIR=/data/imaging_nas/MNI
# run the normalization script on one of the example images to test it out
cd /data/imaging_nas/NACC/MRI/test_run/1.3.12.2.1107.5.2.19.45135.30000019102413580947700000004/1.3.12.2.1107.5.2.19.45135.2019102410105747588520627.0.0.0/


${FSLDIR}/bin/fast -B 1.3.12.2.1107.5.2.19.45135.2019102410105747588520627.0.0.0.nii

# 
#!/bin/sh
#this bash script use fsl to process brain MRI into MNI template

export FSLOUTPUTTYPE='NIFTI'

echo "processing file from $1: $2"

cd $1
cp $2 $3/tmp/

cd $3/tmp/

mkdir /data/imaging_nas/NACC/MRI/test_run_output
export TEST_OUTPUT_DIR=/data/imaging_nas/NACC/MRI/test_run_output
#step1 is to swap axes so that the brain is in the same direction as MNI template.
${FSLDIR}/bin/fslreorient2std 1.3.12.2.1107.5.2.19.45135.2019102410105747588520627.0.0.0.nii $TEST_OUTPUT_DIR/1.3.12.2.1107.5.2.19.45135.2019102410105747588520627.0.0.0.nii

#step2 is to estimate robust field of view
line=`${FSLDIR}/bin/robustfov -i T1.nii | grep -v Final | head -n 1`

x1=`echo ${line} | awk '{print $1}'`
x2=`echo ${line} | awk '{print $2}'`
y1=`echo ${line} | awk '{print $3}'`
y2=`echo ${line} | awk '{print $4}'`
z1=`echo ${line} | awk '{print $5}'`
z2=`echo ${line} | awk '{print $6}'`

x1=`printf "%.0f", $x1`
x2=`printf "%.0f", $x2`
y1=`printf "%.0f", $y1`
y2=`printf "%.0f", $y2`
z1=`printf "%.0f", $z1`
z2=`printf "%.0f", $z2`

#step3 is to cut the brain to get area of interest (roi), sometimes it cuts part of the brain
${FSLDIR}/bin/fslmaths T1.nii -roi $x1 $x2 $y1 $y2 $z1 $z2 0 1 T1_roi.nii
#cp T1.nii T1_roi.nii

#step4: remove skull -g 0.1 -f 0.45
${FSLDIR}/bin/bet T1_roi.nii T1_brain.nii -R

#step5: registration from cut to MNI
${FSLDIR}/bin/flirt -in T1_brain.nii -ref $FSLDIR/data/standard/MNI152_T1_1mm_brain -omat orig_to_MNI.mat
#${FSLDIR}/bin/flirt -in T1_roi.nii -ref $FSLDIR/data/standard/MNI152_T1_1mm -omat orig_to_MNI.mat

#step6: apply matrix onto original image
${FSLDIR}/bin/flirt -in T1.nii -ref $FSLDIR/data/standard/MNI152_T1_1mm_brain -applyxfm -init orig_to_MNI.mat -out T1_MNI.nii

#step7: skull remove -f 0.3 -g -0.0
${FSLDIR}/bin/bet T1_MNI.nii T1_MNI_brain.nii -R -f $4 -g $5

# step8: register the skull removed scan to MNI_brain_only template again to fine tune the alignment
${FSLDIR}/bin/flirt -in T1_MNI_brain.nii -ref $FSLDIR/data/standard/MNI152_T1_1mm_brain -out T1_MNI_brain.nii

#step9: rename and move final file
mv T1_MNI_brain.nii $3/scans/$2

# clear tmp folder
rm -f $3/tmp/*