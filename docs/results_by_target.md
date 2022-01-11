---
layout: default
title: Results by Target
description: Results as broken down by target
---

# Results by Target

Importantly, by using mean rank, as the name implies we are taking the mean over all of the considered target variables.
This is a useful strategy for reducing noise and making the results intelligible, but it can still be useful to look at
the results as averaged only over choice of ML Pipeline. The below figure does exactly that:

[![Results](https://raw.githubusercontent.com/sahahn/parc_scaling/master/analyze/Figures/Figure4.png)](./interactive3.html)

*Click the figure above to open an interactive version of the plot. When using the interactive version of the plot it will be helpful to explore different plotly functionality for limiting the plot to just a subset of targets. To do this try double clicking on a target on the legend, this will isolate the plot to just that target variable. You can then add more by single clicking others, and eventually to reverse the isolation just double click twice on a target.*
{: style="font-size: 85%; text-align: center;"}

We can also look out what happens when we [model](./intro_to_results#modelling-results) these results, interested specifically
in how our fit changes relative to just using the mean rank from the [base results](./base_results.md). Formula: `log10(Mean_Rank) ~ log10(Size)`

{% include by_target_table.html %}

## Increasing Variance

Looking back at the main figure we notice another interesting thing. It appears like as sizes get bigger the spread of values also increases, such that the largest sizes may have the highest mean rank but they also have the highest variability. We can formalize this by computing the [IQR](https://en.wikipedia.org/wiki/Interquartile_range) at every unique size. We can then model this increasing spread as: `IQR ~ log10(Size)`.

{% include iqr_stats.html %}

![IQR](https://raw.githubusercontent.com/sahahn/parc_scaling/master/analyze/Figures/iqr.png)

We actually end up with a pretty good fit explaining increase in IQR at each unique size from log10 of parcel size. One explanation for this is that increasing resolutions helps predict some target variables and not others. In this way, increasing resolution can improve performance on average, but will still sometimes not be a good fit.

## Results Table

Click [here](./results_by_target_table.html) to see the full and sortable raw results as broken down by target variable.
Warning: this table is very large and difficult to make sense of, it may be easier to use the [interactive plot](./interactive3.html).

## Results by Target Cluster

Another interesting way we can break down the results by targets is by first clustering the target variables in order to find groups which are
simmilar. To do this, we use the scikit learn implementation of [FeatureAgglomeration](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.FeatureAgglomeration.html) with linkage='ward'. Note that clustering on targets is performed on only the subject of participants with no missing data for any of the target variables (7,894).

First we try a 4 clustering solution, where we perform clustering separately on the binary and continuous / float variable (2 clusters each), where clusters are:

Float Cluster 1:

 ['Parent Age (yrs)', 'Little Man Test Score', 'Neighborhood Safety', 'NeuroCog PCA1 (general ability)', 'NeuroCog PCA2 (executive function)', 'NeuroCog PCA3 (learning / memory)', 'NIH Card Sort Test', 'NIH List Sorting Working Memory Test', 'NIH Comparison Processing Speed Test', 'NIH Picture Vocabulary Test', 'NIH Oral Reading Recognition Test', 'WISC Matrix Reasoning Score', 'Summed Performance Sports Activity', 'Summed Team Sports Activity']

Float Cluster 2:

 ['Standing Height (inches)', 'Waist Circumference (inches)', 'Measured Weight (lbs)', 'CBCL RuleBreak Syndrome Scale', 'Motor Development', 'Birth Weight (lbs)', 'Age (months)', 'MACVS Religion Subscale']

Binary Cluster 1:

 ['Speaks Non-English Language', 'Months Breast Feds', 'Planned Pregnancy', 'Mother Pregnancy Problems', 'Parents Married', 'Sex at Birth', 'Sleep Disturbance Scale']

Binary Cluster 2:

 ['Thought Problems ASR Syndrome Scale', 'CBCL Aggressive Syndrome Scale', 'Born Premature', 'Incubator Days', 'Has Twin', 'Distress At Birth', 'Any Alcohol During Pregnancy', 'Any Marijuana During Pregnancy', 'KSADS OCD Composite', 'KSADS ADHD Composite', 'Detentions / Suspensions', 'Mental Health Services', 'KSADS Bipolar Composite', 'Prodromal Psychosis Score', 'Screen Time Week', 'Screen Time Weekend']

This subset is plotted below first on a normal scale, then on a log scale, where the mean ranks are determined from averaging just over the target variables in that cluster, and the number in ()'s refers to the number of variables in that cluster.

![base](https://raw.githubusercontent.com/sahahn/parc_scaling/master/analyze/Figures/by_clusters_base.png)
![log](https://raw.githubusercontent.com/sahahn/parc_scaling/master/analyze/Figures/by_clusters_log.png)

We can alternatively cluster over all of the target variables at once (ignoring if binary or not) with an adjustable number of clusters.

- See plots for [5 Clusters](./cluster_targets#5-clusters).
- See plots for [8 Clusters](./cluster_targets#8-clusters).
- See plots for [10 Clusters](./cluster_targets#10-clusters).
- See plots for [13 Clusters](./cluster_targets#13-clusters).

## See Also

- See [All Interactive By Target](./interactive7.html) to see a version of the interactive plot above,
  but with the results from the multiple parcellation strategies added as well.

- Likewise, Click [here](./all_results_by_target_table.html) to see the full and sortable raw results as broken down by target variable,
  with the extra results from the multiple parcellation strategies added - though the [interactive plot](./interactive7.html) may be more legible.