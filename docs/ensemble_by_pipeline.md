---
layout: default
title: Ensemble Results by Pipeline
description: Ensemble Results broken down by pipeline
---

# Ensemble Results by Pipeline

We break down just the [ensemble based multiple parcellation results](./index#multiple-parcellation-strategies) here as both intra and inter pipeline (corresponding to the top and bottom of the figure below).

![By Pipeline](https://raw.githubusercontent.com/sahahn/parc_scaling/master/analyze/Figures/interpipeline_ensemble_comparison.png)

- The top part of the figure, [Intra-Pipeline Comparison](./ensemble_by_pipeline#intra-pipeline-comparison), shows mean rank
  for each ensemble of pipelines as computed only relative to other parcellations evaluated with the same pipeline

- The bottom part of the figure, [Inter-Pipeline Comparison](./ensemble_by_pipeline#inter-pipeline-comparison), shows mean rank as
calculated between each combination.

- The regression line of best fit on the log10-log10 data are plotted separately
  for each pipeline across both figures (shaded regions around the lines of fit represent the bootstrap estimated 95% CI).
  The OLS fit here was with [robust regression](https://www.statsmodels.org/stable/rlm.html).

These results are interesting when contrasted with the same [single parcellation results by pipeline](./by_pipeline.html)]


## Intra-Pipeline

Click [Here](./interactive6.html) for a fullscreen version of the plot.

{% include interactive6.html %}

Note: You can watch an animation of how specific results change with with different pipelines.
You can also hover over specific data points to find out more information. 

The pattern of the intra ensemble stays fairly consistent across pipelines. One interesting trait is that the LGBM based pipeline exhibits the steepest scaling slope.

- Click [here](./ensemble_intrapipe_table.html) to see the full results table containing ensemble inter-pipeline specific results.
- See also Intra-Pipeline results as plotted by raw metric [here](./ensemble_by_pipeline_raw)

## Inter-Pipeline

When looking at inter-pipeline differences, we focus first on just a comparison between the base three pipelines, excluding the 'All' ensembles for now.
Formula: `log10(Mean_Rank) ~ log10(Size) * C(Pipeline)`

{% include ensemble_inter_pipe_stats.html %}

![Inter](https://raw.githubusercontent.com/sahahn/parc_scaling/master/analyze/Figures/ensemble_inter_pipe_stats.png)

We can conclude here that the SVM based ensembles of pipelines outperforms the Elastic-Net and LGBM based ensembles. That said, the differential performance is not quite as large as we saw earlier in the simmilar inter-pipeline single parcellation comparison.

- Click [here](./ensemble_interpipe_table.html) to see the full results table containing ensemble inter-pipeline specific results.

## All Intra-Pipeline

Included below is an interactive intra-pipeline visualization including results across both the single parcellations and multiple parcellations
Click [Here](./interactive5.html) for a fullscreen version of the plot.

{% include interactive5.html %}
