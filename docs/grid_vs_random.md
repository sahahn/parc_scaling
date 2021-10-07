---
layout: default
title: Grid vs. Random
description: Comparison between Grid vs. Random
---

# Grid vs Random

Given the [Results by Target](./results_by_target.html) we know that not one scale of parcellation is going to perform best at all scales (i.e., more parcels isn't always better). 
It therefore seems intuitively like performing a hyper-parameter search over different random parcellations across a range of scales would be a successful strategy.
Likewise, even with a search over fixed scale random parcellations we would expect to be able to atleast do better than just a random parcellation at that same size.
Is this the behavior we end up seeing though? Not quite...

In the below plot we plot only the subset of random parcellations between sizes 100 and 1200 along with the results from the 'Grid' multiple parcellation strategy.

![grid](https://raw.githubusercontent.com/sahahn/parc_scaling/master/analyze/Figures/grid_vs_random.png)

Note that the 'Size' for the Grid multiple parcellation strategy is simply set to be the largest single parcellation within the pool of parcellations. 

We can also formalize the comparison by modelling these same subsets of data points as: `log10(Mean_Rank) ~ log10(Size) * C(Parcellation_Type)`

{% include grid_vs_random.html %}

Even if we treat parcellation type as a fixed effect, the coef. is not significant.
Ultimately we find that that searching over multiple parcellations is not a very effective strategy,
especially when compared against the ensemble based multiple parcellation strategies.
This may relate to a fundamental observed trait in improving ML performance where tuning hyper-parameters
typically is not as efficient as ensembling over multiple estimators. 