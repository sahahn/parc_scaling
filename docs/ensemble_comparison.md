---
layout: default
---

# Ensemble Comparison

From the base [Multiple Parcellations Experiment](./index#multiple-parcellation-strategies) we see that the two ensemble
strategies seem to yield very simmilar results. We can formally test this intuition by [modelling](./intro_to_results#modelling-results)
a subset of the just the ["Voted"](./multiple_parcellations_setup#voted) and ["Stacked"](./multiple_parcellations_setup#stacked) results.
Formula: `log10(Mean_Rank) ~ log10(Size) + C(Parcellation_Type)` (where Parcellation_Type just has two categories)

{% include ensemble_method1.html %}

![Ensemble Method](https://raw.githubusercontent.com/sahahn/parc_scaling/master/analyze/Figures/ensemble_method1.png)

In both the formal statistics and visualizing the results we see no real differences in performance between the two methods.