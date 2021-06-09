---
layout: default
---

## Project Introduction

Different parcellations and neuroimaging atlases are ubiquitous in neuroimaging, namely because they allow for a principled
reduction of features (which has its own sleuth of benefits). This project focuses in particular on the question of
choice of parcellation, in particular, how does choice of parcellation influence performance
within a machine learning context (See [Background on Machine Learning for Neuroimaging](./ml_neuroimaging.html)). We
perform a number of different experiments in order to probe this and related questions in detail.

## Base Experiment Setup

The base experiment conducted within this project was a systematic test of different pre-defined parcellations performance.
The structure of the evaluation is shown below:

![Base Exp Structure](https://raw.githubusercontent.com/sahahn/Parcs_Project/master/analyze/Figures/Figure1.png)

- a). This study uses baseline data from the ABCD Study [NDA Collection 3165 Release](https://collection3165.readthedocs.io/en/stable/).
Specifically, we concatenate participants structural MRI measures to use as input features for ML (See [Input Data](./input_data.html) for more information).

- b). We test a mix of mostly random and existing parcellations (See [Parcellations](./parcellations.html)).

- c). Three different ML pipelines are used, each based on a different popular base estimator (See [ML Pipelines](./ml_pipelines.html)).

- d). In total we employ 45 different phenotypic target variables (See [Target Variables](./variables.html)).

We evaluated each combination of target variable, parcellation and ML pipeline with five-fold
cross validation using the full set of available participants. The 5-fold fold structure was kept
constant and therefore directly comparable across all combinations of ML pipeline, target variable and parcellation. 
This evaluation procedure was used to generate different metrics of performance,
[explained variance](https://scikit-learn.org/stable/modules/model_evaluation.html#explained-variance-score)
for regression predictors and
[area under the receiver operator characteristic curve (ROC AUC)](https://scikit-learn.org/stable/modules/model_evaluation.html#roc-metrics)
for binary predictors, for each of the combinations.
Performance metrics are then converted in the results into a measure of [Mean Rank](./results_intro#mean-rank).

## Base Experiment Results

The below figure plots performance, as represented by [mean relative ranking](./results_intro#mean-rank)
between all 220 parcellations, against the number of parcels / size in each parcellation.
Results are further colored by type of parcellation and a log10-log10 inset
of the same plot provided. It may be useful to also review [Intro to Results](./results_intro.html) first, which
provides a gentle introduction to the format plotted below.

![Base Results](https://raw.githubusercontent.com/sahahn/Parcs_Project/master/analyze/Figures/Figure2.png)

- There is a relationship between performance, as estimated by [mean rank](./results_intro#mean-rank), and parcellation size.
  Up to ~Size 4000 a [power law](./estimate_powerlaw.html) relationship appears to hold, with scaling exponent .-2753.
  
- [Existing parcellations](./parcellations#existing-parcellations) outperformed [randomly generated parcellations](./parcellations#random-parcellations)
  when controlling for the influence of size, however [Existing parcellations](./parcellations#existing-parcellations) tended to have fewer parcels 
  than our results suggest to be most predictive.

- The general pattern is stable across [ML Pipelines](./ml_pipelines.html), but when compared inter-pipeline,
  the SVM based pipeline is most competitive (See [By Pipeline](./by_pipeline.html)).

- Notably, performance may not in practice be the only metric of interest,
  instead there are a number of [Performance Trade-Offs](./trade_offs.html) to consider, e.g.,
  runtime and downstream interpretation complexity.

- See also [Interactive Results](./results.html).



## Authors

Sage Hahn, ... 

## Acknowledgments 

... 