---
layout: default
title: Parcellations
description: All parcellations used
---

# Parcellations

Within this project we consider two main sources for surface parcellations, existing and random.
Lastly, a few additional variants are tested including downsampled and as extracted directly from FreeSurfer.

[Final Parcellations Used](https://github.com/sahahn/parc_scaling/tree/main/parcels) (excluded a few too large parcellations).
These are saved as numpy arrays corresponding the fs_LR_32K space, in the case of probabilistic parcellation are
saved with shape (64984, number of parcels), otherwise are saved as a flat array of 64984 vertex (left hemi first).

## Existing Parcellations

All considered surface parcellations were converted, if necessary,
in the FS LR 32K standard left and right hemisphere standard vertex space.
Existing parcellations were sourced from as many places as possible. “Soft” volumetric parcellations were re-sampled by projecting each map separately.
To re-sample “hard” volumetric parcellations, we first converted them to “soft” parcellations and then once ultimately in fs LR 32k space,
the “hard” parcellation was reconstructed by assigning each vertex to the parcel with the highest “soft” value.
Once parcellations were projected into fsaverage space, these parcellations, in addition to a
collection of others which could only be found in fsaverage space, were re-sampled to fs LR 32k space with tools available
for the Human Connectome Project Workbench (Marcus, 2011). See setup/process_parcs.py for the script to re-sample parcellations.

{% include parcel_table.html %}

See also the folder [raw/](https://github.com/sahahn/parc_scaling/tree/main/raw) which contains the 'raw' existing parcellations,
included information on how they can be downloaded. 

## Random Parcellations

This project uses the idea of random surface parcellations extensively. Random parcellations are generated as follows: For a random parcellation of size N, N random points are first selected at random across both hemisphere’s 59,412 vertices (medial wall vertices excluded). Each selected point is then assigned as the seed of a new region and is randomly assigned a size probability between 0 and 1. Next, a region is randomly selected according to a weighted random choice between all regions (e.g., if a region was assigned an initial probability of .5 it would be picked on average twice as often as a region assigned .25). A random vertex is then added to the selected region from the list of valid neighboring unassigned vertices. This sequence, of selecting a region and adding one valid vertex, is repeated until all regions have no unassigned neighbors and therefore all non-medial wall vertices are assigned to a region. 

Example generated random parcellation:

![Random Parc Gif](https://raw.githubusercontent.com/sahahn/Parcs_Project/master/data/rand_parc.gif)

Note: The above example, in contrast to the random parcellations generated in this project,
is in fsaverage5 space (vs. fs_LR_32k) and doesn't mask the medial wall (the medial wall is masked in this project).

Source code for generating random parcellations is implemented and available through
the [Brain Predictability toolbox (BPt)](https://github.com/sahahn/BPt),
specifically [here](https://github.com/sahahn/BPt/blob/master/BPt/extensions/random_parcellation.py).

Random parcellations within this project are generated in the setup/process_random_parcels.py script. Random parcellations
are used as a part of the base

## Extra Parcellations

We also tested 5 different downsampled icosahedron parcellations.
These span in size from 42 to 1002 regions per hemisphere. Finally, we assessed the
Desikan and Destrieux ROI values as extracted by FreeSurfer. These differ from the
other tested parcellations both in how values are generated (FreeSurfer extracts values in
an individual's native space whereas we extract values from data warped to a common space)
in addition to the surface modalities used (only average thickness, surface area and mean curvature
are employed, which differs from the features used in the base analyses). 
