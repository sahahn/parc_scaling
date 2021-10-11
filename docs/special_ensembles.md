---
layout: default
title: Special Ensembles
description: Additional consideration for ensembles over subsets of existing parcellations.
---

# Special Ensembles

Given some of the insights from ([best strategies across different sizes](./whats_best.html)), a natural- maybe kind of wacky extension- is to say:
"What happens when you ensembles across existing parcellations?

In this section we do exactly that, ensembling across 6 special subsets of existing parcellations.

- schaefer:
    
    The 10 [Schaefer Parcellations](./parcels_viz#schaefer) ranging in size
    from 100-1000.

- mist:
    
    The 9 [MIST Parcellations](./parcels_viz#mist) ranging in size from 7 to 444.

- basc
    
    The 9 [BASC Parcellations](./parcels_viz#basc) ranging in size from 9 to 444.
  
- difumo
    
    The 5 probabilistic / soft [DiFuMo Parcellations](parcels_viz#difumo) ranging
    in sizes from 64 to 1024.
  
- icosahedron
    
    The 6 [Icosahedron Parcellations](./parcels_viz#icosahedron) ranging in
    sizes from 42 to 1442.
  
- existing:
    
    All of the 82 [Existing Parcellations](./parcellations.html). Note: not
    including the Icosahedron based parcellations.
  
## Stacked Ensemble

Plotted below is a comparison between just the base stacking ensembles across random parcellations (both from fixed and across sizes)
in contrast with those from these 6 special combinations of parcellations:

![X](https://raw.githubusercontent.com/sahahn/parc_scaling/master/analyze/Figures/special_stacking.png)

In this case, we note that most combinations of special parcellation ensembles appear to fit right into the expected scaling (with some deviance),
and that the ensemble over all 82 existing parcellations outperforms any other.

## Voted Ensemble

Plotted below is a comparison between just the base voting ensembles across random parcellations (both from fixed and across sizes)
in contrast with those from these 6 special combinations of parcellations:

![X](https://raw.githubusercontent.com/sahahn/parc_scaling/master/analyze/Figures/special_voting.png)

Here we note that the special voting ensembles over combinations of existing parcellations appear to outperform, as adjusted for size, their
randomly generated counterparts. Also relative to the stacking based, where we saw that the ensemble over all 82 parcellations was the new
top performer, we did not see this behavior with the voting ensemble. This could be a result of the stacking ensemble able to filter through and not
weight some of the poor performing results well in the ensemble, whereas the voting ensemble always weights everything equally.

## Grid Ensemble

Plotted below is a comparison between just the base grid searches across random parcellations (both from fixed and across sizes)
in contrast with those from these 6 special combinations of parcellations:

![X](https://raw.githubusercontent.com/sahahn/parc_scaling/master/analyze/Figures/special_grid.png)

The grid search based results show that the strategy of searching over special ensembles is somewhat effective, and scales generally about as expected.

## Highest Performing Comparison

In order to evaluate the 'All' ensemble with these special combinations of pooled existing parcellations,
we will consider a modified versions of the 
plot / comparisons performed [here in the what's best section](./whats_best.html).
The difference here is that the voted and stacked SVM and 'All'
ensembles are included as valid comparisons (along with all of the same results as before).

![special](https://raw.githubusercontent.com/sahahn/parc_scaling/master/analyze/Figures/special_highest.png)

It's a bit hard from this plot to parse out exactly which specific new / from the special ensembles are most competitive,
so it is likely worthwhile to consider this plot along with the sortable table of results below.


## Results Table

This table includes just results from the subsets as plotted above - i.e., the same
subsets as the best of section, but with the added special ensembles included.

The [mean relative rankings](./results_intro#mean-rank) shown here are 
as computed only between these subsets (and as  averaged across [target variable](./variables.html)).
averaged across  and computed across parcellation and [ML pipeline](./ml_pipelines.html).
Mean R2 and ROC AUC are calculated only from their relevant subsets
of 22 and 23 [target variables](./variables.html) respectively. 

- Warning: Mean R2 and ROC AUC should be taken with a grain of salt due to [scaling issues](./scaling_issues.html) between different targets.

- See Also [Multiple Parcellations Naming](./multiple_parcellations_setup#on-naming).

*Table columns are sortable!*
{: style="font-size: 85%; text-align: center;"}

{% include best_of_full_results_extra.html %}