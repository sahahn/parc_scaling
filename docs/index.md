---
layout: default
---

## Project Introduction

Different parcellations and neuroimaging atlases are ubiquitous in neuroimaging, namely because they allow for a principled
reduction of features (which has its own sleuth of benefits). This project focuses in particular on the question of
choice of parcellation, in particular, how does choice of parcellation influence performance
within a machine learning context (See [Background on Machine Learning for Neuroimaging](./ml_neuroimaging.html)). We
perform a number of different experiments in order to probe this question in detail.

## Docs Introduction

This documentation leans heavily on hyper-links to different pages, so for more information on different
pieces of the project or specific ideas / concepts, please follow the provided hyper-links. These will links
to either other project documentation pages or in some cases key external references or specific code. Also note that the
'back' button on your browser or opening links in new tabs may be useful strategies for navigating this page as there
is no side navigation bar.

## Base Experiment Setup

The base experiment conducted within this project was a systematic test of different pre-defined parcellations performance.
The structure of the evaluation is shown below:

![Base Exp Structure](https://raw.githubusercontent.com/sahahn/Parcs_Project/master/analyze/Figures/Figure1.png)

- a). This study uses data from the ABCD Study release [NDA Collection 3165](https://collection3165.readthedocs.io/en/stable/).
Specifically, we concatenate structural MRI measures to use as input features (See [Input Data](./input_data.html) for more information).

- b). We test a mix of mostly random and existing parcellations (See [Parcellations](./parcellations.html)).

- c). Three different ML pipelines are used, each based on a different popular base estimator (See [ML Pipelines](./ml_pipelines.html)).

- d). In total we employ 45 different phenotypic target variables (See [Target Variables](./variables.html)).

In order to evaluate a given target variable, parcellation or machine learning strategy’s relative performance,
we defined an explicit framework in which different combinations of methods could be compared.
We evaluated each combination of target variable, parcellation and ML pipeline with five-fold
cross validation using the full set of available participants.
Each of the validation folds, including any nested parameter tuning folds,
were conducted such that participants from the same family
were preserved within the same training or testing fold. The 5-fold fold structure was kept
constant and therefore comparable across
all combinations of ML pipeline, target variable and parcellation. In the case of
missing target variables, those participants with missing data were simply excluded from their respective
training or validation fold. This strategy was used to generate different metrics of performance,
[explained variance](https://scikit-learn.org/stable/modules/model_evaluation.html#explained-variance-score) for regression predictors
and [area under the receiver operator characteristic curve (ROC AUC)](https://scikit-learn.org/stable/modules/model_evaluation.html#roc-metrics)
for binary predictors, for each of the proposed combinations.

## Base Experiment Results

[Results](./results.html)

[Performance Trade-Offs](./trade_offs.html)

## Authors

Sage Hahn, ... 

## Acknowledgments 

... 