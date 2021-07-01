---
layout: default
title: Input Data
description: Information of the input data used.
---

## Input Data

Data is sourced from the baseline ABCD Study release [NDA Collection 3165 Release 1.1.0](https://collection3165.readthedocs.io/en/stable/).
Data used within this study are the sMRI outputs of a modified HCP style pipeline.
We downloaded for each available subject their left and right hemisphere curvature,
sulcal depth, cortical thickness and unsmoothed myelin map, each in the standard
[FS LR 32k vertex space](https://emmarobinson01.com/2016/02/10/unofficial-guide-to-the-hcp-surface-file-formats/).
Likewise, we additionally downloaded each subject's automatically computed
[FreeSurfer ROI stats](https://fscph.nru.dk/slides/Martin/fs.roi.mr.pdf) files. 

We chose to use [structural MRI](https://www.sciencedirect.com/topics/medicine-and-dentistry/structural-magnetic-resonance-imaging)
surfaces. That said, the idea of parcellations easily extends to
task-based fMRI and resting state fMRI just as easily as dMRI. The choice to use structural
MRI surfaces was therefore somewhat arbitrary, but given its ubiquity and the amount of
available studies which employ it, it may not be a bad choice. Future work may very
well consider different modalities or explicitly [multi-modal fusion](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4917230/).

## Downloading

In order to download the used data, we employed the following download tool:
[NDA ABCD Downloader](https://github.com/DCAN-Labs/nda-abcd-s3-downloader).
The following subjects of data were specified when downloading for all available subjects:

- derivatives.anat.space-fsLR32k_curv
- derivatives.anat.space-fsLR32k_desc-smoothed_myelinmap
- derivatives.anat.space-fsLR32k_myelinmap
- derivatives.anat.space-fsLR32k_sulc
- derivatives.anat.space-fsLR32k_thickness
- derivatives.anat.stats

The data is then moved to the [raw/](https://github.com/sahahn/parc_scaling/tree/main/raw) folder upon successful download.
Unfortunately, due to data privacy issues, this data cannot be shared directly. If interested in working with ABCD Study data, please
find more information on their website [https://abcdstudy.org/](https://abcdstudy.org/).