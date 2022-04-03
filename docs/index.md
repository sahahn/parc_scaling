---
layout: default
title: Performance Scaling for Structural MRI Surface Parcellations
description: A Machine Learning Analysis in the ABCD Study
---

## Project Introduction

Parcellations and neuroimaging atlases are ubiquitous in neuroimaging, namely because they allow for a principled
reduction of features. This project focuses in particular on the question of
choice of parcellation, in particular, how does choice of parcellation influence performance
within a machine learning context (See [Goals / Considerations for Machine Learning Based Neuroimaging](./ml_neuroimaging.html)).
We perform a number of different experiments in order to probe this and related questions in detail.

This website acts as both a standalone project site and as online supplementary materials for
the corresponding project paper - [*Why a website?*](./website_info.html)

## Base Experiment Setup

The base experiment conducted within this project was a systematic test of performance of different pre-defined parcellations. The structure of the evaluation is shown below:

![Outline](https://raw.githubusercontent.com/sahahn/parc_scaling/master/analyze/Figures/Figure1.png)

- a). This study uses baseline data from the ABCD Study [NDA Collection 3165 Release](https://collection3165.readthedocs.io/en/stable/).
Specifically, we concatenate 9,432 participant's structural MRI measures to use as input features for ML (See [Input Data](./input_data.html) for more information).

- b). We test a mix of mostly random and existing parcellations (See [Parcellations](./parcellations.html)).

- c). Three different ML pipelines are used, each based on a different popular base estimator (See [ML Pipelines](./ml_pipelines.html)).

- d). In total we employ 45 different phenotypic target variables (See [Target Variables](./variables.html)).

We [evaluated](./evaluation_structure.html) each combination of target variable, parcellation and ML pipeline with five-fold
cross validation using the full set of available participants. The CV fold structure was kept
constant and therefore directly comparable across all combinations of ML pipeline, target variable and parcellation. 
This evaluation procedure was used to generate different metrics of performance,
[R2](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.r2_score.html#sklearn.metrics.r2_score)
for regression predictors and
[area under the receiver operator characteristic curve (ROC AUC)](https://scikit-learn.org/stable/modules/model_evaluation.html#roc-metrics)
for binary predictors, for each of the combinations.
Performance metrics were then converted in the results into a measure of [Mean Rank](./results_intro#mean-rank).

## Base Experiment Results

The below figure plots performance, as measured by [mean relative ranking](./results_intro#mean-rank)
between all 220 parcellations, against the number of parcels / size in each parcellation.
Results are further colored by type of parcellation and a log10-log10 inset
of the same plot is provided. It may be useful to also review the [Intro to Results](./results_intro.html) page first, which
provides a gradual introduction to the format the results are plotted with below.

[![Base Results](https://raw.githubusercontent.com/sahahn/parc_scaling/master/analyze/Figures/Figure2.png)](./interactive1.html)

*Click the figure above to open an interactive version of the plot*
{: style="font-size: 85%; text-align: center;"}

- There is a relationship between performance, as measured by [mean relative ranking](./results_intro#mean-rank), and parcellation size.
  Up to ~Size 4000 a [power law](./estimate_powerlaw.html) relationship appears to hold, with [scaling exponent](./powerlaw_scaling_exp.html) .-2753.
  See [results table](./base_results#results-table).
  
- [Existing parcellations](./parcellations#existing-parcellations) outperformed [randomly generated parcellations](./parcellations#random-parcellations)
  when controlling for the influence of size, however [existing parcellations](./parcellations#existing-parcellations) tended to have fewer parcels 
  than our results suggest to be most predictive (See [Results by Parcellation Type](./base_results#parcellation-type-as-fixed-effect)).

- The general pattern was stable across [ML Pipelines](./ml_pipelines.html), but when compared inter-pipeline,
  the [SVM](./ml_pipelines#svm) based pipeline was most competitive. See [Results by Pipeline](./by_pipeline.html).

- How stable are these results across different target variables? See [Results by Target](./results_by_target.html).


## Multiple Parcellation Strategies

As an additional set of analyses we sought to characterize the potential gains in performance from employing strategies that can
make use of information from multiple parcellations in order to inform predictions.
These extensions to the base analysis can be broken up into three different types:
choice of parcellation as a nested hyper-parameter - (["Grid"](./multiple_parcellations_setup#grid)),
ensembling over multiple parcellations using voting - (["Voted"](./multiple_parcellations_setup#voted)),
and ensembling using stacking - (["Stacked"](./multiple_parcellations_setup#stacked)).
See [Multiple Parcellations Setup](./multiple_parcellations_setup.html) for more detailed information on how this experiment was structured.

The figure below compares the prior single parcellation only results to the introduced [multiple parcellation strategies](./multiple_parcellations_setup.html).
The plotted [mean ranks](./results_intro#mean-rank) are therefore computed now between 412 (220 single parcellation and 192 multiple parcellation based) configurations. 
The results are further broken down by if the pool of parcellations was sourced from fixed sizes or across multiple sizes
(See [Multiple Parcellations Evaluation](./multiple_parcellations_setup#evaluation)).

[![Multiple Parcellation Results](https://raw.githubusercontent.com/sahahn/parc_scaling/master/analyze/Figures/Figure5.png)](./interactive4.html)
*Click the figure above to open an interactive version of the plot*
{: style="font-size: 85%; text-align: center;"}

- Ensemble methods across multiple parcellations outperform single parcellation based methods (See [Single vs. Ensembled Parcellations](./single_vs_ensemble.html)).

- We did not observe a large difference between ensemble strategies [Voted](./multiple_parcellations_setup#voted)
  and [Stacked](./multiple_parcellations_setup#stacked) - [unless we breakdown results by binary vs. regression!](./ensemble_comparison.html)

- Sourcing random parcellation for ensembling from fixed sizes outperforms sourcing parcellations
  from a range of sizes (See [Fixed vs. Across Sizes](./ensemble_comparison#fixed-vs-across-sizes)).

- The [SVM](./ml_pipelines#svm) based ensembles were once again better than the others,
  with the exception now of the special 'All' ensemble. See [Ensemble Results by Pipeline](./ensemble_by_pipeline.html).

- Searching over multiple parcellations as hyper-parameter was not a successful strategy.
  See [Grid vs. Random](./grid_vs_random.html).

- All options considered, what are the [best strategies across different sizes](./whats_best.html)?

## Discussion Points

- There is certainly a relationship between parcellation scale and performance,
  but [what factors influence this relationship?](.performance_scaling.html)

- [Why do we see a performance boost from increasing parcellation resolution?](./why_performance_boost.html)

- This project makes a lot of different comparisons, with this in mind we provide some
  [practical recommendations for researchers.](./recommendations.html)
  
- [Why does ensembling over multiple parcellations help?](./why_ensemble_boost.html)

- Notably, performance may not in practice be the only metric of interest,
  instead there are a number of [Performance Trade-Offs](./trade_offs.html) to consider, e.g.,
  runtime and downstream interpretation complexity.

- This project required an incredible amount of computations, but we also
  made a great deal of effort to [optimize performance](./optimizations.html) wherever possible.

- There are a number of [possible extensions / future work](./future_work.html).

## Conclusion

In testing a variety of [parcellation schemes](./parcellations.html) and [ML modeling](./ml_pipelines.html) approaches, we have identified an apparent [power law scaling]((./estimate_powerlaw.html)) of increasing predictive performance by increasing parcellation resolution. The details of this relationship were found to vary according to [type of parcellation](./base_results#parcellation-type-as-fixed-effect) as well as [ML pipeline](./by_pipeline.html) employed, though the general pattern proved stable. The [large sample size](./input_data#sample-size), range of predictive [targets](./variable.html), and collection of [existing]((./parcellations#existing-parcellations)) and [random parcellations](./parcellations#random-parcellations) tested all serve to lend confidence to the observed results. Researchers selecting a parcellation for predictive modelling may wish to consider this size-performance trade-off in addition to other factors such as [interpretability and computational resources](./trade_offs.html). We also highlighted important factors that improved performance above and beyond the size-scaling, for example, finding [existing parcellations performed better than randomly generated parcellations](./base_results.html). Further, we demonstrated the benefit of [ensembling over multiple parcellations](./single_vs_ensemble.html), which yielded a performance boost relative to results from single parcellations.


## Authors

[Sage Hahn](https://github.com/sahahn), [Max M. Owens](https://scholar.google.com/citations?user=DxYosOMAAAAJ&hl=en), [DeKang Yuan](https://www.researchgate.net/scientific-contributions/DeKang-Yuan-2168133545), [Anthony C Juliano](https://scholar.google.com/citations?user=tYsQsskAAAAJ&hl=en), [Alexandra Potter](https://www.uvm.edu/cas/psychology/profiles/alexandra-potter-behavior-therapy-and-psychotherapy), [Hugh Garavan](https://www.uvm.edu/cas/psychology/profiles/hugh-garavan),
[Nicholas Allgaier](http://www.uvm.edu/~nallgaie/)

Departments of [Complex Systems](https://vermontcomplexsystems.org/) and [Psychiatry](http://www.med.uvm.edu/psychiatry/home), University of Vermont, Burlington, VT 05401
 

## Acknowledgments 

- Sage Hahn, Max M. Owens, DeKang Yuan and Anthony C Juliano were supported by NIDA grant [T32DA043593](https://vermontcomplexsystems.org/education/complexbrain/)

- Data used in the preparation of this article were obtained from the [ABCD Study](https://abcdstudy.org) held in the NDA. This is a multisite, longitudinal study designed to recruit more than 10,000 children ages 9–10 years old and follow them over 10 years into early adulthood. The ABCD study is supported by the National Institutes of Health and additional federal partners under award numbers U01DA041048, U01DA050989, U01DA051016, U01DA041022, U01DA051018, U01DA051037, U01DA050987, U01DA041174, U01DA041106, U01DA041117, U01DA041028, U01DA041134, U01DA050988, U01DA051039, U01DA041156, U01DA041025, U01DA041120, U01DA051038, U01DA041148, U01DA041093, U01DA041089, U24DA041123 and U24DA041147. A full list of supporters is available at https://abcdstudy.org/federal-partners.html. A listing of participating sites and a complete listing of the study investigators can be found at https://abcdstudy.org/consortium_members/.

- Computations were performed on the [Vermont Advanced Computing Core](https://www.uvm.edu/vacc) supported, in part, by NSF award number OAC-1827314.

- We would also like to thank the other members of the Hugh Garavan lab for their support throughout this project.

![t32 logo](https://raw.githubusercontent.com/sahahn/parc_scaling/master/data/t32_logo.png){: width="250" } ![abcd logo](https://raw.githubusercontent.com/sahahn/parc_scaling/master/data/abcd-study-logo.png){: width="250" } ![vacc logo](https://raw.githubusercontent.com/sahahn/parc_scaling/master/data/vacc_logo.jpg){: width="250" }


## Site Map

This project website is surprisingly expansive when considering nested hyper-links. Listed below are links in alphabetical order to all main site pages (many of which include multiple sub-sections):

- [All Results by Target Table Results ](all_results_by_target_table.html)
- [All Raw Results by Pipeline](all_by_pipeline_raw.html)
- [All Targets](target_variables.html)
- [Base Results Size Differences](size_differences.html)
- [Base Results](./base_results.html)
- [Base Results Extra](./base_results_extra.html)
- [Effects of Feature Selection](effect_of_fs.html)
- [Ensemble Comparison](ensemble_comparison.html)
- [Ensemble Inter-Pipe Table Results](ensemble_interpipe_table.html)
- [Ensemble Intra-Pipe Table Results](ensemble_intrapipe_table.html)
- [Ensemble Raw Intra-Pipeline Comparison](./ensemble_by_pipeline_raw)
- [Ensemble Results by Pipeline](ensemble_by_pipeline.html)
- [Estimate Powerlaw](estimate_powerlaw.html)
- [Evaluation Structure](evaluation_structure.html)
- [Full Table Results ](full_results.html)
- [Future Work](future_work.html)
- [Grid vs. Random](grid_vs_random.html)
- [Input Data](input_data.html)
- [Inter-Pipeline Table Results](interpipe_table.html)
- [Interactive Figure 1](interactive1.html)
- [Interactive Figure 1 R2](interactive1_r2.html)
- [Interactive Figure 1 ROC AUC](interactive1_roc_auc.html)
- [Interactive Figure 2](interactive2.html)
- [Interactive Figure 2 Base](interactive2_base.html)
- [Interactive Figure 2 R2](interactive2_r2.html)
- [Interactive Figure 2 Base R2](interactive2_base_r2.html)
- [Interactive Figure 2 ROC AUC](interactive2_roc_auc.html)
- [Interactive Figure 2 Base ROC AUC](interactive2_base_roc_auc.html)
- [Interactive Figure 3](interactive3.html)
- [Interactive Figure 3 R2](interactive3_r2.html)
- [Interactive Figure 3 ROC AUC](interactive3_roc_auc.html)
- [Interactive Figure 4](interactive4.html)
- [Interactive Figure 4 R2](interactive4_r2.html)
- [Interactive Figure 4 ROC AUC](interactive4_roc_auc.html)
- [Interactive Figure 5](interactive5.html)
- [Interactive Figure 5 Base](interactive5_base.html)
- [Interactive Figure 5 R2](interactive5_r2.html)
- [Interactive Figure 5 Base R2](interactive5_base_r2.html)
- [Interactive Figure 5 ROC AUC](interactive5_roc_auc.html)
- [Interactive Figure 5 Base ROC AUC](interactive5_base_roc_auc.html)
- [Interactive Figure 6](interactive6.html)
- [Interactive Figure 6 Base](interactive6_base.html)
- [Interactive Figure 6 R2](interactive6_r2.html)
- [Interactive Figure 6 Base R2](interactive6_base_r2.html)
- [Interactive Figure 6 ROC AUC](interactive6_roc_auc.html)
- [Interactive Figure 6 Base ROC AUC](interactive6_base_roc_auc.html)
- [Interactive Figure 7](interactive7.html)
- [Interactive Figure 7 R2](interactive7_r2.html)
- [Interactive Figure 7 ROC AUC](interactive7_roc_auc.html)
- [Intra-Pipeline Table Results](intrapipe_table.html)
- [Intro to Results](results_intro.html)
- [ML Pipelines](ml_pipelines.html)
- [ML for Neuroimaging](ml_neuroimaging.html)
- [Multiple Parcellation Strategies Setup](multiple_parcellations_setup.html)
- [Outliers](outliers.html)
- [Parcellations Viz](parcels_viz.html)
- [Parcellations](parcellations.html)
- [Performance Optimizations](optimizations.html)
- [Performance Scaling](performance_scaling.html)
- [Raw Intra-Pipeline Comparison](./by_pipeline_raw)
- [Recommendations](recommendations.html)
- [Resampling Parcellations](resample_parcellations.html)
- [Results by Clusters of Targets](cluster_targets.html)
- [Results by Pipeline](./by_pipeline.html)
- [Results by Pipeline Median](./by_pipeline_median.html)
- [Results by Target Table Results ](results_by_target_table.html)
- [Results by Target](results_by_target.html)
- [Scaling Exponent](powerlaw_scaling_exp.html)
- [Scaling Issues](scaling_issues.html)
- [Single vs. Ensembled Parcellations](single_vs_ensemble.html)
- [Special Ensembles](special_ensembles.html)
- [Target Variables](variables.html)
- [Trade-Offs](trade_offs.html)
- [Website Info](website_info.html)
- [Whats best?](whats_best.html)
- [Why a performance boost?](why_performance_boost.html)
- [Why ensemble boost?](why_ensemble_boost.html)
  