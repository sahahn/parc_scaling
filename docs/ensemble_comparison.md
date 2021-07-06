---
layout: default
title: Ensemble Comparison
---

# Ensemble Comparison

## Voted Vs Stacked

From the base [Multiple Parcellations Experiment](./index#multiple-parcellation-strategies) we see that the two ensemble
strategies seem to yield very simmilar results. We can formally test this intuition by [modelling](./intro_to_results#modelling-results)
a subset of the just the ["Voted"](./multiple_parcellations_setup#voted) and ["Stacked"](./multiple_parcellations_setup#stacked) results.
Formula: `log10(Mean_Rank) ~ log10(Size) + C(Parcellation_Type)` (where Parcellation_Type just has two categories)

{% include ensemble_method1.html %}

We can also model allowing for interactions: `log10(Mean_Rank) ~ log10(Size) * C(Parcellation_Type)`

{% include ensemble_method2.html %}

![Ensemble Method](https://raw.githubusercontent.com/sahahn/parc_scaling/master/analyze/Figures/ensemble_method1.png)

In both the formal statistics and visualizing the results we see no significant differences in performance between the two methods,
or significant interactions with Size.

- See also [full results table](./full_results.html).

## More to the story?

Interestingly, if we go to the [sortable results table](./full_results.html) and sort by the default [mean rank](./results_intro#mean-rank) we
find a mix of voted and stacked. If we sort by Mean R2 though... we find that all of the top results are from the stacking ensemble,
and by Mean ROC AUC the opposite, all of the top results are from the voting ensemble.

We can more formally investigate this by running separate comparisons on just the binary target variables and just the regression based ones.
First let's look at the regression only:

{% include ensemble_method_regression.html %}
![Ensemble Method](https://raw.githubusercontent.com/sahahn/parc_scaling/master/analyze/Figures/ensemble_method_regression.png)

Now the binary only:

{% include ensemble_method_binary.html %}
![Ensemble Method](https://raw.githubusercontent.com/sahahn/parc_scaling/master/analyze/Figures/ensemble_method_binary.png)

Hun, so which ensemble method works better actually ends up depending on if the prediction is regression or binary based.
This could be related to some trait of binary optimization problems vs. regression... but it could also just be a problem or bug in the
implementation of the stacking ensemble for binary variables. For now we will just tentatively present these results as is.

## Fixed vs Across Sizes

Using again the subset of just ["Voted"](./multiple_parcellations_setup#voted)
and ["Stacked"](./multiple_parcellations_setup#stacked) results we can investigate
a different question, namely, does the sourcing of the base parcellations matter? Specifically, is there a difference in ensemble based methods which draw from parcellations with all the same fixed size versus parcellations from a range of sizes? (See [Multiple Parcellation Evaluation](./multiple_parcellations_setup#evaluation) for more details. We create binary flag variable `Across_Sizes` to represent if results are from across multiple resolutions or not.

Formula: `log10(Mean_Rank) ~ log10(Size) + C(Across_Sizes)`

{% include fixed_vs_across.html %}
![Ensemble Method](https://raw.githubusercontent.com/sahahn/parc_scaling/master/analyze/Figures/fixed_vs_across.png)

These results seem to suggest that Fixed Sizes work better than across sizes given the same number of unique total regions of interest (noting that Size for ensembles is calculated as the sum of each pooled parcellations Size / unique regions of interest).

We can also check for interactions with Size, but first we will restrict the results to only the overlapping sizes. Then model as `log10(Mean_Rank) ~ log10(Size) * C(Across_Sizes)`

{% include fixed_vs_across2.html %}
![Ensemble Method](https://raw.githubusercontent.com/sahahn/parc_scaling/master/analyze/Figures/fixed_vs_across2.png)

These results indicate that not only do fixed size parcellations do better, but they exhibit different scaling with respect to size.
The biggest caveat to all of these comparisons being that the different sizes for fixed sizes
and ranges of sizes for across sizes were hardly comprehensive. 