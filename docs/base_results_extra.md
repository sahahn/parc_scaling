---
layout: default
title: Base Results Extra
description: Extra Results by Parcellation Type
---

# Extra Results by Parcellation Type

As an alternative modelling choice to the results explored in [base results](./base_results.html) we could instead of using
formula `log10(Mean_Rank) ~ log10(Size) + C(Parcellation_Type)`, instead use either `log10(Median_Rank) ~ log10(Size) + C(Parcellation_Type)`,
`log10(Max_Rank) ~ log10(Size) + C(Parcellation_Type)` or `log10(Min_Rank) ~ log10(Size) + C(Parcellation_Type)`. The key variable changing here being
the use of median, max or min to summarize ranks, instead of mean rank. Importantly, in this case, the mean or average is still used to summarize across Pipelines, and as in
the base comparison we still [estimate the region where a powerlaw holds](./estimate_powerlaw.html) and only model the results within this range, but with the
alternate formulation of averaged rank.

## Mean Rank

For ease of comparison we again provide the results from the Mean Rankings here.

{% include base_results1.html %}
![fits](https://raw.githubusercontent.com/sahahn/parc_scaling/master/analyze/Figures/base_results_fit1.png)

## Median Rank

{% include base_results1_median.html %}

As with mean rank, we have only the significant coef. between [existing] and [random] parcellations - we plot
below just these two lines of fit, as estimated by the OLS, and colored by parcellation type.

![fits](https://raw.githubusercontent.com/sahahn/parc_scaling/master/analyze/Figures/base_results_fit1_median.png)

As might be expected, the difference between mean and median ranks ends up being pretty small. Interesting, we actually
end up with a more robust power-law scaling fit when using median, as well as a larger size range in which the relationship holds.

A recreation of the main figure from the index page, but with median rank is provided here:

![base](https://raw.githubusercontent.com/sahahn/parc_scaling/master/analyze/Figures/Figure2_median.png)

## Max Rank

Using Max Rank is actually quite different than using mean or median. Instead, what max ranks tells us is essentially the worst case performance of a parcellation across target variables, 

{% include base_results1_max.html %}

To match the plot above, and to limit the complexity of the plot, we just show fits for existing and random type parcellations.

![fits](https://raw.githubusercontent.com/sahahn/parc_scaling/master/analyze/Figures/base_results_fit1_max.png)

A recreation of the main figure from the index page, but with max rank is provided here:

![base](https://raw.githubusercontent.com/sahahn/parc_scaling/master/analyze/Figures/Figure2_max.png)

## Min Rank

Using Min Rank is similarly different to Mean and Median like Max Rank, but describes the best case performance.

{% include base_results1_min.html %}

To match the plot above, and to limit the complexity of the plot, we just show fits for existing and random type parcellations.

![fits](https://raw.githubusercontent.com/sahahn/parc_scaling/master/analyze/Figures/base_results_fit1_min.png)

A recreation of the main figure from the index page, but with min rank is provided here:

![base](https://raw.githubusercontent.com/sahahn/parc_scaling/master/analyze/Figures/Figure2_min.png)
