---
layout: default
title: Re-sample
---

For this project we gathered a large collection of different [Existing Parcellations](./parcellations#existing-parcellations),
which often required various re-s

As some parcellations were only originally available in volumetric MNI space, we applied registration fusion to map these parcellations to fsaverage space based on scripts available from Wu et al. (Wu, 2018). From fsaverage surface space, resampling to FS LR 32k space was conducted with tools available from the Human Connectome Project Workbench (Marcus, 2011). Depending on the type and original space of the parcellation a number of different strategies were necessary, a more complete description of the steps taken in each case are provided on the paper’s supplemental web page (sahahn.github.io/parc_scaling).


All considered surface parcellations were converted, if necessary,
in the FS LR 32K standard left and right hemisphere standard vertex space.
Existing parcellations were sourced from as many places as possible.
“Soft” volumetric parcellations were re-sampled by projecting each map separately.
To re-sample “hard” volumetric parcellations, we first converted them
to “soft” parcellations and then once ultimately in fs LR 32k space,
the “hard” parcellation was reconstructed by assigning each
vertex to the parcel with the highest “soft” value.
Once parcellations were projected into fsaverage space, these parcellations, in addition to a
collection of others which could only be found in fsaverage space,
were re-sampled to fs LR 32k space with tools available
for the [Human Connectome Project Workbench](https://www.humanconnectome.org/software/connectome-workbench).