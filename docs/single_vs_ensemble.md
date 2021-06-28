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

The take-away here is that there is a clear benefit in employing ensembles across multiple parcellations especially relative to using the
information from a single parcellation. This benefit importantly takes into account that most of the tested ensemble methods have more unique parcels than
their single parcellation counterparts. The other point of interest is that these ensembles were all generated using random parcellations,
which [previous results](./base_results.html) showed to be much worse than existing parcellations - which serves to highlight even further
the benefit from ensembling.

- What about between different types of ensembles? Do we see the a difference in performance there? [Link](./ensemble_comparison.html).

- We can also look at different sourcing for parcellation sizes (i.e., fixed versus across sizes) [Link](./ensemble_comparison#fixed-vs-across-sizes).

- See also [full results table](./full_results.html) 