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