---
layout: default
title: By Pipeline
description: Results broken down by pipeline
---

# By Pipeline

We break down the [base results](./base_results.md) here by pipeline (instead of parcellation type) in two different ways:
Intra and Inter pipeline (corresponding to the top and bottom of the figure below).

*If necessary first view the [intro to results](./results_intro.html)
for an example on how to interpret the below figure.*
{: text-align: center;"}

![By Pipeline](https://raw.githubusercontent.com/sahahn/parc_scaling/master/analyze/Figures/Figure3.png)

- The top part of the figure, Intra-Pipeline Comparison, shows mean rank
  for each pipeline as computed only relative to other parcellations evaluated with the same pipeline

- The bottom part of the figure, Inter-Pipeline Comparison, shows mean rank as
  calculated between each parcellation-pipeline combination

- The regression line of best fit on the log10-log10 data are plotted separately
  for each pipeline across both figures (shaded regions around the lines of fit represent the bootstrap estimated 95% CI).
  The OLS fit here was with robust regression.

## Intra-Pipeline Comparison

When comparing in an intra-pipeline fashion, we are essentially computing the ranks independently for each choice of [ML Pipeline](./ml_pipelines.html). We also [estimate the powerlaw region](./estimate_powerlaw.html) separately for each. 

- Elastic-Net: 7-2000
- SVM: 20-4000
- LGBM: 7-3000

We can then [model](./intro_to_results#modelling-results) these results as `log10(Mean_Rank) ~ log10(Size) * C(Pipeline_Type)` where Pipeline_Type is a fixed effect and can interact with Size.

{% include intra_results1.html %}

![By Pipeline](https://raw.githubusercontent.com/sahahn/parc_scaling/master/analyze/Figures/intra_plot1.png)

Another interesting way to view how results change when computed separately between pipelines is through an interactive visualization. 
{% include interactive2.html %}

[Fullscreen Plot Link](./interactive2.html)
{: style="font-size: 85%; text-align: center;"}

A nice feature of the interactive plot is that by selecting different pipelines from the toggle, you can watch an animation of how specific results change
with with different pipelines. You can also hover over specific data points to find out more information, for example what parcellation that data point corresponds to.

## Inter-Pipeline Comparison

Alternately, we can compute rankings in an inter-pipeline manner, which means that the initial calculating of Rank is determined by directly comparing all Pipeline-Parcellation pairs for each target variable. The different here being inter-pipeline's Mean Rank as out of 660 versus intra as out of 220.

We model these results in the same way as with the intra-pipeline comparison, but importantly using the different computation of [mean rank](./intro_to_results#mean-rank). We also in this case do not estimate a powerlaw region of scaling as here we are more interested in the full statistical comparison. Formula: `log10(Mean_Rank) ~ log10(Size) * C(Pipeline_Type)`. 

{% include inter_results1.html %}

![By Pipeline](https://raw.githubusercontent.com/sahahn/parc_scaling/master/analyze/Figures/inter_plot1.png)