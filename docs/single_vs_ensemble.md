---
layout: default
---

# Single vs. Ensembled Parcellations

We can [model](./intro_to_results#modelling-results) the results from the [Multiple Parcellations Experiment](./multiple_parcellations_setup.html)
with a focus on teasing apart performance differences between single vs. ensembled parcellations. Specifically we create
a binary flag for any results which were ensembled (in this case treating ["Grid"](./multiple_parcellations_setup#grid) as not ensembled), and
model as: `log10(Mean_Rank) ~ log10(Size) * Is_Ensemble`.

{% include is_ensemble_stats.html %}

The difference is even more obvious when explicitly plotted.

![Is Ensemble](https://raw.githubusercontent.com/sahahn/parc_scaling/master/analyze/Figures/is_ensemble.png)