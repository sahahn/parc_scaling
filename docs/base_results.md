---
layout: default
title: Base Results
description: Base results for single parcellations
---

# Single Parcellation Results

## Parcellation Type As Fixed Effect

To model the base results with respect to type of parcellation we use an [OLS regression](./intro_to_results#modelling-results), with
the formula `log10(Mean_Rank) ~ log10(Size) + C(Parcellation_Type)`, so notably first treating choice of parcellation as a fixed effect.
We first though [estimate the region where a powerlaw holds](./estimate_powerlaw.html) and only model the results within this range.

{% include base_results1.html %}

We note here the significant coef. between [existing] and [random] parcellations - we plot
below just these two lines of fit, as estimated by the OLS, and colored by parcellation type.

![fits](https://raw.githubusercontent.com/sahahn/parc_scaling/master/analyze/Figures/base_results_fit1.png)

## Parcellation Type As Interaction

We can also alternately model parcellation type as as both a fixed effect and with a possible interaction with Size. 

{% include base_results2.html %}

We see that in this case none of the interactions with Size are significant.

![fits](https://raw.githubusercontent.com/sahahn/parc_scaling/master/analyze/Figures/base_results_fit1.png)

Plotting the basic fits by [parcellation type](./parcellations.html) we can see that for parcellations types with only a few samples
it is difficult to conclude anything as the sample size is not sufficient.

A key point of interest beyond comparing between parcellation type is the coef. for Size.
This represents the [scaling exponent](./powerlaw_scaling_exp.html) in a
powerlaw relationship between Size and Performance.
Lastly, exploring the [interactive plot](./interactive1.html) may be useful seeing how any one parcellation did.


## Results Table

The table below includes all parcellations specific scores.

{% include raw_results1.html %}