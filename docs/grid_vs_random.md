---
layout: default
---

# Grid vs Random

Given the [Results by Target](./results_by_target.html) we know that not one scale of parcellation is going to perform best at all scales (i.e., more parcels isn't always better). 
It therefore seems intuitively like performing a hyper-parameter search over different random parcellations, especially across a range of scales, would be a successful strategy.
Likewise, even with a search over fixed scale random parcellations we would expect to be able to atleast do better than just a random parcellation at that same size.
Is this the behavior we end up seeing though? Not quite...

In the below plot we plot only the subset of random parcellations between sizes 100 and 1200 along with the results from the 'Grid' multiple parcellation strategy.