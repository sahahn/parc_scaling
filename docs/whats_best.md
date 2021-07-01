---
layout: default
title: Whats best
description: Across different scales what performs best
---

## Whats best?

Across different pieces of the analyses we have established a number of different interesting, but perhaps hard to piece together results.
For example, [existing parcellations perform better than random parcellations](./base_results.html).
This section of the project site is designed to focus in on only a subset of the results as informed by these prior findings.
The foundational points are as follows:

- [Existing parcellations perform better than random parcellations](./base_results.html)
- [SVM based pipelines were most competitive for single parcellations](./by_pipeline.html)
- [SVM based pipelines were also most competitive for ensembled parcellations](./ensemble_by_pipeline#inter-pipeline-comparison)
- [Fixed size ensembles outperformed across sizes'](./ensemble_comparison#fixed-vs-across-sizes)

Based on those findings, we plot two special subsets:

1. Existing single parcellation results from only the SVM based pipeline (SVM Non-Random Existing)
2. Fixed size only ensembled parcellation results from only the SVM based pipeline (SVM Ensemble)

The last plotted is the special 'All' ensembled results, which ensembles
over both pipeline and parcellation (See [Multiple Parcellations Evaluation](./multiple_parcellations_setup#evaluation)).

![Best](https://raw.githubusercontent.com/sahahn/parc_scaling/master/analyze/Figures/Figure6.png)

## Results Table

This table includes just results from the subsets as plotted above. The [mean relative rankings](./results_intro#mean-rank) shown here are 
as computed only between these subsets (and as  averaged across [target variable](./variables.html)).
averaged across  and computed across parcellation and [ML pipeline](./ml_pipelines.html).
Mean R2 and ROC AUC are calculated only from their relevant subsets
of 22 and 23 [target variables](./variables.html) respectively. Warning: Mean R2 and ROC AUC should
be taken with a grain of salt due to [scaling issues](./scaling_issues.html) between different targets.

*Table columns are sortable!*
{: style="font-size: 85%; text-align: center;"}

{% include best_of_full_results.html %}

See Also [Multiple Parcellations Naming](./multiple_parcellations_setup#on-naming).