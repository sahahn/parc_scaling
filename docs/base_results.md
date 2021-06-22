---
layout: default
title: Base Results
description: Base results for single parcellations
---

# By Parcellation Type Results

[![Base Results](https://raw.githubusercontent.com/sahahn/parc_scaling/master/analyze/Figures/Figure2.png)](./interactive1.html)

To model the base results with respect to type of parcellation we use an [OLS regression](./intro_to_results#modelling-results), with
the formula `log10(Mean_Rank) ~ log10(Size) + C(Parcellation_Type)`, so notably first treating choice of parcellation as a fixed effect.
We first though [estimate the region where a powerlaw holds](./estimate_powerlaw.html) and only model the results within this range. This procedure 

{% include base_results1.html %}

We can also alternately model parcellation type as as both a fixed effect and with a possible interaction with Size. 

{% include base_results2.html %}

We see that in this case none of the interactions with Size are significant.

[fits](https://raw.githubusercontent.com/sahahn/parc_scaling/master/analyze/Figures/base_results_fit1.png)

Plotting the basic fits by [parcellation type](./parcellations.html) we can see that for parcellations types with only a few samples
it is difficult to conclude anything as the sample size is not sufficient.