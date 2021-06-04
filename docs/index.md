---
layout: default
---

## Project Introduction

Different parcellations and neuroimaging atlases are ubiquitous in neuroimaging, namely because they allow for a principled reduction of features (which has its own sleuth of benefits). This project focuses in particular on the question of choice of parcellation, in particular, how does choice of parcellation influence performance within a machine learning context.

[Background on Machine Learning for Neuroimaging](./ml_neuroimaging.html)

The base experiment conducted within this project was a systematic test of different pre-defined parcellations performance. The structure of the test is shown below:

![Base Exp Structure](https://raw.githubusercontent.com/sahahn/Parcs_Project/master/analyze/Figures/Figure1.png)

## Input Data

Data from the ABCD Study release 2, NDA Collection 3165 (See: https://collection3165.readthedocs.io/en/stable/). Data used within this study are the sMRI outputs of a modified HCP style pipeline. We downloaded for each available subject their left and right hemisphere curvature, sulcal depth, cortical thickness and unsmoothed myelin map, each in the standard FS LR 32k vertex space. Likewise, we additionally downloaded each subject's automatically computed FreeSurfer ROI stats files. 

We chose to use structural MRI surfaces. That said, the idea of parcellations easily extends to task-based fMRI and resting state fMRI just as easily as dMRI. The choice to use structural MRI surfaces was therefore somewhat arbitrary, but given its ubiquity and the amount of available studies which employ it, it may not be a bad choice. That said, future work may very well consider different modalities or explicitly multi-modal fusion.


## Target Variables

A collection of 45 target phenotypic variables (23 binary and 22 continuous), used to gauge predictive performance, was sourced from the second ABCD Study release. Variables were sourced directly from the rds file made available by the DAIRC (specifically on a version of the rds file saved as a csv). All collected variables, both target and brain, are from the baseline time point on the study. Best efforts were made to source a list of representative, diverse and predictive variables. Towards this effort, a larger list of variables was originally screened on a subset of the data (n=2000) to avoid including variables not at all predictive from sMRI measures.


| Variable Name                         |
|:--------------------------------------|
[Standing Height (inches)](./target_variables#standing-height-inches)|
[Waist Circumference (inches)](./target_variables#waist-circumference-inches)|               
[Measured Weight (lbs)](./target_variables#measured-weight-lbs)|
[CBCL RuleBreak Syndrome Scale](./target_variables#cbcl-rulebreak-syndrome-scale)|                     
[Parent Age (yrs)](./target_variables#parent-age-yrs)|                      
[Motor Development](./target_variables#motor-development)|                      
[Birth Weight (lbs)](./target_variables#birth-weight-lbs)|                               
[Age (months)](./target_variables#age-months)|                                        
[Little Man Test Score](./target_variables#little-man-test-score)|                                
[MACVS Religion Subscale](./target_variables#macvs-religion-subscale)|                             
[Neighborhood Safety](./target_variables#neighborhood-safety)|                               
[NeuroCog PCA1 (general ability)](./target_variables#NeuroCog PCA1 (general ability))|                   
[NeuroCog PCA2 (executive function)](./target_variables#NeuroCog PCA2 (executive function))|
[NeuroCog PCA3 (learning / memory)](./target_variables#NeuroCog PCA3 (learning / memory))|
[NIH Card Sort Test](./target_variables#NIH Card Sort Test)|
[NIH List Sorting Working Memory Test](./target_variables#NIH List Sorting Working Memory Test)|
[NIH Comparison Processing Speed Test](./target_variables#NIH Comparison Processing Speed Test)|
[NIH Picture Vocabulary Test](./target_variables#NIH Picture Vocabulary Test)|
[NIH Oral Reading Recognition Test](./target_variables#NIH Oral Reading Recognition Test)|
[WISC Matrix Reasoning Score](./target_variables#WISC Matrix Reasoning Score)|
[Summed Performance Sports Activity](./target_variables#Summed Performance Sports Activity)|
[Summed Team Sports Activity](./target_variables#Summed Team Sports Activity)|

----

### Parcellations

Within this project we test a mix of 

All considered surface parcellations were converted, if necessary, in the FS LR 32K standard left and right hemisphere standard vertex space. We consider two main sources for surface parcellations, existing and random. Lastly, a few additional variants are tested including downsampled and as extracted directly from FreeSurfer.

{% include parcel_table.html %}

<td><strong><span style="text-decoration:underline;">Name</span></strong>
</p>
   </td>
   <td><strong><span style="text-decoration:underline;"># of Parcellations</span></strong>
</p>
   </td>
   <td><strong><span style="text-decoration:underline;">Type</span></strong>
</p>
   </td>
   <td><strong><span style="text-decoration:underline;">Reference</span></strong>
</p>
   </td>
   <td>Schaefer Local-global parcellation
</p>
   </td>
   <td>10 (scales 100-1000)
</p>
   </td>
   <td>Hard
</p>
   </td>
   <td>Schaefer 2018
</p>
   </td>
   <td>Gordon
</p>
   </td>
   <td>3 (different sources)
</p>
   </td>
   <td>Hard
</p>
   </td>
   <td>Gordon 2016
</p>
   </td>
   <td>Brodmann Areas
</p>
   </td>
   <td>1
</p>
   </td>
   <td>Hard
</p>
   </td>
   <td>Brodmann 1909
</p>
   </td>
   <td>VDG11b
</p>
   </td>
   <td>1
</p>
   </td>
   <td>Hard
</p>
   </td>
   <td>Van Essen 2012
</p>
   </td>
   <td>HCP-MMP
</p>
   </td>
   <td>3 (different sources)
</p>
   </td>
   <td>Hard
</p>
   </td>
   <td>Glasser 2016
</p>
   </td>
   <td>Automatic Anatomical Labeling (AAL)
</p>
   </td>
   <td>2 (different sources)
</p>
   </td>
   <td>Hard
</p>
   </td>
   <td>Tzourio-Mazoyer 2002
</p>
   </td>
   <td>Baldassano
</p>
   </td>
   <td>1
</p>
   </td>
   <td>Hard
</p>
   </td>
   <td>Baldassano 2015
</p>
   </td>
   <td>Desikan
</p>
   </td>
   <td>2 (different sources)
</p>
   </td>
   <td>Hard
</p>
   </td>
   <td>Desikan 2006
</p>
   </td>
   <td>Destrieux
</p>
   </td>
   <td>2 (different sources)
</p>
   </td>
   <td>Hard
</p>
   </td>
   <td>Destrieux 2010
</p>
   </td>
   <td>Brainnetome
</p>
   </td>
   <td>2 (different sources)
</p>
   </td>
   <td>Hard
</p>
   </td>
   <td>Fan 2016
</p>
   </td>
   <td>Power
</p>
   </td>
   <td>2 (different sources)
</p>
   </td>
   <td>Hard 
</p>
   </td>
   <td>Power 2011
</p>
   </td>
   <td>Shen 268 Parcels
</p>
   </td>
   <td>2 (different sources)
</p>
   </td>
   <td>Hard
</p>
   </td>
   <td>Shen 2013
</p>
   </td>
   <td>Shen 368 Parcels
</p>
   </td>
   <td>1
</p>
   </td>
   <td>Hard
</p>
   </td>
   <td>Salehi 2020
</p>
   </td>
   <td>Yeo
</p>
   </td>
   <td>3 (7 Networks, 17 Networks and parcel level version)
</p>
   </td>
   <td>Hard
</p>
   </td>
   <td>Yeo 2014
</p>
   </td>
   <td>DiFuMo
</p>
   </td>
   <td>5 (scales 64-1028)
</p>
   </td>
   <td>Soft
</p>
   </td>
   <td>Dadi 2020
</p>
   </td>
   <td>MIST
</p>
   </td>
   <td>9 (scales 9-444)
</p>
   </td>
   <td>Hard
</p>
   </td>
   <td>Urchs 2019
</p>
   </td>
   <td>AICHA
</p>
   </td>
   <td>1
</p>
   </td>
   <td>Hard
</p>
   </td>
   <td>Joliot 2015
</p>
   </td>
   <td>Economo
</p>
   </td>
   <td>1
</p>
   </td>
   <td>Hard
</p>
   </td>
   <td>von Economo 2915
</p>
   </td>
   <td>NSPN500
</p>
   </td>
   <td>1
</p>
   </td>
   <td>Hard
</p>
   </td>
   <td>Whitaker 2016
</p>
   </td>
   <td>Oasis
</p>
   </td>
   <td>1
</p>
   </td>
   <td>Hard
</p>
   </td>
   <td>Sabuncu 2011
</p>
   </td>
   <td>SJH
</p>
   </td>
   <td>1
</p>
   </td>
   <td>Hard
</p>
   </td>
   <td>Harrison 2015
</p>
   </td>
   <td>Allen
</p>
   </td>
   <td>1
</p>
   </td>
   <td>Soft
</p>
   </td>
   <td>Allen 2011
</p>
   </td>
   <td>BASC
</p>
   </td>
   <td>9 (scales 9-444)
</p>
   </td>
   <td>Soft
</p>
   </td>
   <td>Bellec 2013
</p>
   </td>
   <td>MSDL
</p>
   </td>
   <td>1
</p>
   </td>
   <td>Soft
</p>
   </td>
   <td>Varoquaux 2011
</p>
   </td>
   <td>Harvard-Oxford
</p>
   </td>
   <td>4 (different versions)
</p>
   </td>
   <td>Soft
</p>
   </td>
   <td>Jenkinson 2012
</p>
   </td>
   <td>Craddock
</p>
   </td>
   <td>4 (different versions)
</p>
   </td>
   <td>Soft
</p>
   </td>
   <td>Craddock 2012
</p>
   </td>
   <td>Smith ICA
</p>
   </td>
   <td>2 (different versions)
</p>
   </td>
   <td>Soft
</p>
   </td>
   <td>Smith 2009
</p>
   </td>
   <td>CPAC
</p>
   </td>
   <td>1
</p>
   </td>
   <td>Hard
</p>
   </td>
   <td>Craddock 2013
</p>
   </td>
   <td>Hammersmith
</p>
   </td>
   <td>1
</p>
   </td>
   <td>Hard
</p>
   </td>
   <td>Hammers 2003
</p>
   </td>
   <td>JuBrain
</p>
   </td>
   <td>1
</p>
   </td>
   <td>Hard
</p>
   </td>
   <td>Eickhoff 2005
</p>
   </td>
   <td>MICCAI
</p>
   </td>
   <td>1
</p>
   </td>
   <td>Hard
</p>
   </td>
   <td>http://www.neuromorphometrics.com/2012_MICCAI_Challenge_Data.html
</p>
   </td>
   <td>Slab
</p>
   </td>
   <td>2 (907 and 1068)
</p>
   </td>
   <td>Hard
</p>
   </td>
   <td>Sripada 2014
</p>
   </td>
   <td>Princeton Visual
</p>
   </td>
   <td>1
</p>
   </td>
   <td>Hard
</p>
   </td>
   <td>Wang 2015
</p>
   </td>

----

### Machine Learning (ML)

We employ three base ML pipelines, each with classifier and regressor variants, as a representative sample of different popular and predictive ML strategies. All machine learning experiments are conducted with BPt. Each pipeline is first composed of a loading component responsible for extracting ROIs according to the specified surface parcellation. The output from the loading step concatenates the extracted ROI values across each of the different surface values, generating a feature vector of length four times the number of parcels for each subject. Next, the ROI values are scaled using robust scaling, where each feature is standardized by first removing the median and then scaling according to the 5th and 95th percentiles of that features distribution. These features are then used as input to train a classifier or regressor under one of three different base configurations, these are:


#### Elastic-Net
The base model within the pipeline under this configuration is a logistic or linear regression with elastic-net penalty available from scikit-learn. A nested random hyper-parameter search over 60 combinations is evaluated through nested 3-fold CV to select the strength of regularization applied as well as the ratio between l1 and l2 regularization.

    param_search = Param_Search(search_type='RandomSearch', n_iter=60,
                                splits=3, n_repeats=1, cv=cv)

    model = Model('elastic', params=1,
                  param_search=param_search,
                  extra_params={'tol': 1e-3})

#### SVM
The base model within the pipeline under this configuration is a Support Vector Machine (SVM) classifier or regressor with radial basis function kernel available from scikit-learn. A front end univariate feature selection procedure was further added to this pipeline configuration (based on the ANOVA f-value between a feature and the target variable). A nested random hyper-parameter search over 60 combinations is then evaluated through nested 3-fold CV in order to select the SVM’s strength of regularization and kernel coefficient as well as the percent of features to keep in the front-end feature selector. All three hyper-parameters are optimized at the same time.

    param_search = Param_Search(search_type='RandomSearch', n_iter=60,
                                splits=3, n_repeats=1, cv=cv,
                                search_only_params={'svm classifier__probability': False})

    feat_selector =\
            [Feat_Selector('variance threshold'),
             Feat_Selector('univariate selection', params=2)]

    nested_svm_pipe =\
        Model_Pipeline(feat_selectors=feat_selector,
                       model=Model('svm', params=1, extra_params={'cache_size': 2000}),
                       param_search=param_search)

    model = Model(nested_svm_pipe)


#### LGBM
The base model optimized is an extreme gradient boosted tree based classifier and regressor from the Light Gradient Boosting Machine (LGBM) package. The tuned hyper-parameters for this model included the type of boosting, the number of estimators, different tree sampling parameters, and regularization parameters. Given the high number of hyper-parameters to tune, 9, in contrast to the other base models, we employed a two point differential evolution based hyper-parameter search strategy implemented through the python library Nevergrad. The search was run for 180 iterations, where each set of parameters is evaluated with a single 25% nested validation split.


    lgbm_param_search =\
            Param_Search(search_type='TwoPointsDE', n_iter=180,
                         splits=0.25, n_repeats=1, cv=cv)

    model = Model('light gbm', params=1, param_search=lgbm_param_search)

----

[Results](./results.html)

[Neuro-Imaging for ML Background and Motivation](./ml_neuroimaging.html)

[Random Parcellations](./random_parcellations.html)

[Performance Trade-Offs](./trade_offs.html)