# Parcellation Project

It is common to analyze surface-based neuroimaging data, and likewise for a number of reasons to reduce surface data to a collection of representative regions of interest. What about when one is interested in performing machine learning? Is there a best pre-defined parcellation to use? This project seeks to answer that question.

The base experiment conducted within this project is a systematic test of different pre-defined parcellations performance. There are some key decision though which greatly influence the experiment.

-----

### Directory structure

This project is setup with a few different directories. In general those starting with capital letters, (Setup/, Exp/, Plots/) contain code used to run different steps, where lowercase directories are for data (data/, parcels/, ect...).

-----

### Input Data

Data from the ABCD Study release 2, NDA Collection 3165 (See: https://collection3165.readthedocs.io/en/stable/). Data used within this study are the sMRI outputs of a modified HCP style pipeline. We downloaded for each available subject their left and right hemisphere curvature, sulcal depth, cortical thickness and unsmoothed myelin map, each in the standard FS LR 32k vertex space. Likewise, we additionally downloaded each subject's automatically computed FreeSurfer ROI stats files. 

We chose to use structural MRI surfaces. That said, the idea of parcellations easily extends to task-based fMRI and resting state fMRI just as easily as dMRI. The choice to use structural MRI surfaces was therefore somewhat arbitrary, but given its ubiquity and the amount of avaliable studies which employ it, it may not be a bad choice. That said, future work may very well consider different modalities or explicitly multi-modal fusion.

----

### Target Variables

A collection of 45 target phenotypic variables (23 binary and 22 continuous), used to gauge predictive performance, was sourced from the second ABCD Study release. Variables were sourced directly from the rds file made available by the DAIRC (specifically on a version of the rds file saved as a csv). All collected variables, both target and brain, are from the baseline time point on the study. Best efforts were made to source a list of representative, diverse and predictive variables. Towards this effort, a larger list of variables was originally screened on a subset of the data (n=2000) to avoid including variables not at all predictive from sMRI measures. 

See [setup_ML_Logs/Exp/](https://github.com/sahahn/Parcs_Project/tree/main/Setup/setup_ML_Logs/My_Exp) whichlists all target variables used and shows their distribution.

----

### Parcellations

All considered surface parcellations were converted, if necessary, in the FS LR 32K standard left and right hemisphere standard vertex space. We consider two main sources for surface parcellations, existing and random. Lastly, a few additional variants are tested including downsampled and as extracted directly from FreeSurfer.


This project uses the idea of random surface parcellations extensively. 

<img src="https://raw.githubusercontent.com/sahahn/Parcs_Project/master/data/rand_parc.gif"/>


----

### How were the different machine learning (ML) algorithms chosen?


----
