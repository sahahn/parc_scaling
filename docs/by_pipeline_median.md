---
layout: default
title: Results by Pipeline Median
description: Results broken down by pipeline with median rank
---

# Results by Pipeline Median

This page goes over again the [By Pipeline](./by_pipeline.html) results, but uses Median Rank from [Alternative ranks](./results_intro#alternative-ranks) instead of Mean Rank.
As before, we show both an Intra and Inter pipeline (corresponding to the top and bottom of the figure below).

![By Pipeline](https://raw.githubusercontent.com/sahahn/parc_scaling/master/analyze/Figures/Figure3_median.png)

- The top part of the figure, Intra-Pipeline Comparison, shows median rank
  for each pipeline as computed only relative to other parcellations evaluated with the same pipeline

- The bottom part of the figure, Inter-Pipeline Comparison, shows median rank as
  calculated between each parcellation-pipeline combination.

- The regression line of best fit on the log10-log10 data are plotted separately
  for each pipeline across both figures (shaded regions around the lines of fit represent the bootstrap estimated 95% CI).
  The OLS fit here was with [robust regression](https://www.statsmodels.org/stable/rlm.html).

Specific statistical tables and results are re-created below.

## Intra-Pipeline Comparison

{% include intra_results1_median.html %}
![By Pipeline](https://raw.githubusercontent.com/sahahn/parc_scaling/master/analyze/Figures/intra_plot1_median.png)


## Inter-Pipeline Comparison


{% include inter_results1_median.html %}
![B](https://raw.githubusercontent.com/sahahn/parc_scaling/master/analyze/Figures/inter_plot1_median.png)
