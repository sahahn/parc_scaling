---
layout: default
title: Resampling Parcellations
description: Information of on resampling of parcellations was performed.
---

# Resampling Parcellations

For this project we gathered a large collection of different [Existing Parcellations](./parcellations#existing-parcellations),
which often required various resampling procedures depending on their native space and type (e.g., 'Hard' vs. 'Soft').
The different procedures decided upon are listed below. That said, some parcellation were already in this space and only needed
minimal pre-processing (e.g., converting from saved matlab arrays, or concatenating lh and rh files saved separate).

## Resampling from FreeSurfer Standard Space

From fsaverage surface space, resampling to fs LR 32k space was conducted
with tools available from the Human Connectome Project Workbench (Marcus, 2011).
See wrapper function
[surf_to_surf](https://github.com/sahahn/parc_scaling/blob/607b4dbec6248bfdc1d78950e162556bb2e28fc5/setup/helpers.py#L148).
This command has alternate versions with flag '-label-resample' for resampling static / hard parcellations and 
'-metric-resample' for resampling each parcel of a probabilistic parcellation. 

Once in fs LR 32k space we further masked out the medial wall for all parcellations according to the defined
medial wall in fs LR 32k space.

## Resampling from Volumetric Standard Space

The Brainnetome parcellation is used here as an example of a static parcellation originally in volumetric space
that must be resampled to fs LR 32k surface space.

![Full Volume](https://raw.githubusercontent.com/sahahn/parc_scaling/master/extra/Figures/full_volume.png)

To re-sample static / “hard” volumetric parcellations, we first converted them
to “soft” parcellations, in practice treating each region of interest as a separate volume
(where that region is labelled with 1 and everywhere else 0).

![First ROI](https://raw.githubusercontent.com/sahahn/parc_scaling/master/extra/Figures/volume_one_roi.png)

These separate volumes are then individually
resampled using [Registration Fusion](https://github.com/ThomasYeoLab/CBIG/tree/master/stable_projects/registration/Wu2017_RegistrationFusion)
a technique from Wu et al. 2018. The result of this resampling is that ROI as projected to fsaverage space.

![FreeSurfer](https://raw.githubusercontent.com/sahahn/parc_scaling/master/extra/Figures/freesurfer_surface_one_roi.png)

Next, each ROI is resampled from fsaverage space to fs LR 32k space in the same manner as with surfaces
[originally in fsaverage space](./resample_parcellations#resampling-from-freesurfer-standard-space).

![FS_LR_32](https://raw.githubusercontent.com/sahahn/parc_scaling/master/extra/Figures/fs_lr_surface_one_roi.png)

The above process is repeated for all ROIs separately, then in order to re-combine them, a simple argmax operation is carried
out across all separate ROI's surfaces, where each vertex is assigned to the ROI with the highest value.

![all rois](https://raw.githubusercontent.com/sahahn/parc_scaling/master/extra/Figures/full_resample.png)

Lastly, the medial wall is masked out, according to the medial mall defined by FS LR 32k space.

![final](https://raw.githubusercontent.com/sahahn/parc_scaling/master/extra/Figures/final_no_medial_wall.png)


## Code

The 'meat' of the exact code used to re-sample parcellations can be found at [setup/helpers.py](https://github.com/sahahn/parc_scaling/tree/main/setup/helpers.py) which includes the
source code for functions called to process specific parcellations in script
[setup/process_parcs.py](https://github.com/sahahn/parc_scaling/tree/main/setup/process_parcs.py). The
functions contained here are for the most part python wrappers around different command line tools. For example:

~~~ python

    def conv_to_gifti(lh_loc, rh_loc):

        temp_name = 'temp'

        setup_fs_loc = os.path.join(freesurfer_loc, 'SetUpFreeSurfer.sh')

        fs_cmd = 'source ' + setup_fs_loc
        
        lh_gifti = 'L.' + temp_name + '.gii'
        rh_gifti = 'R.' + temp_name + '.gii'

        # Write full command to temp file and run
        with open('temp.sh', 'w') as f:
            f.write(fs_cmd + ' && ')
            f.write('mri_convert ' + lh_loc + ' ' + lh_gifti + ' && ')
            f.write('mri_convert ' + rh_loc + ' ' + rh_gifti)

        os.system('bash temp.sh')
        os.remove('temp.sh')
        os.remove(lh_loc)
        os.remove(rh_loc)

        return lh_gifti, rh_gifti

~~~

Which is used to convert surface files from freesurfer format to gifti via the freesurfer command
[mri_convert](https://surfer.nmr.mgh.harvard.edu/fswiki/mri_convert).

## Libraries / External Code Used

The re-sampling required the use of a number of external libraries including:

- [nibabel](https://nipy.org/nibabel/) and [nilearn](https://nilearn.github.io/)
- [Human Connectome Project Workbench](https://www.humanconnectome.org/software/connectome-workbench)
- [FreeSurfer](https://surfer.nmr.mgh.harvard.edu/)
- [Registration Fusion](https://github.com/ThomasYeoLab/CBIG/tree/master/stable_projects/registration/Wu2017_RegistrationFusion)