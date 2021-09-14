---
layout: default
title: Performance Scaling
---

# There is a relationship between parcellation scale and performance

## Power-Law Scaling

One of the key goals of this work was describing the relationship between spatial scale (i..e, number of parcels) and predictive performance.
That some relationship exists at all is abundantly clear from a range of [results](./index#base-experiment-results) presented.
The interesting piece is how this relationship appears to follow a power-law scaling,
though the details of this scaling can vary with choice of pipeline and parcellation strategy.
We identified scaling across roughly 3 orders of magnitude (~10-4000) with
coefficients between ¼ and ⅓ (exact coefficient dependent on specific setup).
We further tested how stable this relationship was when compared in an intra-pipeline fashion, finding that the general pattern was preserved.
That said, the SVM-based results varied significantly from the other two pipelines,
with a more steep estimated scaling coefficient and a larger estimated region of scaling,
which may be a result of the front-end feature selection portion of the SVM pipeline. 

## By Pipeline

We also explored the influence of choice of ML pipeline.
For parcellations larger than size ~100 the SVM based pipeline outperformed all other pipelines and
for those less than ~100 the Elastic-Net pipeline.
Whereas the LGBM tree-based pipeline was not competitive at any size,
an observation inline with recent work based on sMRI ML on UK Biobank participants (Schulz 2020).
We also investigate one potential explanation for why the SVM outperforms the other pipelines, that is
[is the front-end univariate feature selection responsible for improved scaling?](./effect_of_fs.html) as that
is a piece only added to the SVM based pipeline. In short, we found that this was not the case.


While perhaps interesting conceptually, treating choice of parcellation as a nested hyper-parameter,
in practice, yielded lackluster results, especially when compared with the ensemble based methods.
We observed that this approach fell closely in line with expected random parcellation performance at the same size.
In contrast, we observed a significant performance improvement from the multiple parcellation ensemble
based strategies when compared to the single parcellation only results.
Notably, the ensemble based random parcellations continue to exhibit scaling beyond the ~4000
range where scaling was estimated to have ended with respect in analyses with single parcellations.
These results establish the merit in constructing ensembles across multiple parcellations to achieve maximal predictive performance.
Specifically, we found no significant differences in predictive performance between the voting and stacking ensemble approaches tested.
We did observe significant differences between ensembles with random parcellations of the same size versus ensembles with parcellations of multiple sizes, in this case finding that the fixed size parcellations on average performed better.
Therefore, to maximize predictive performance and computational demands, we recommend that,
of the ensemble methods tested, fixed size parcellations with a voting ensemble be used in future work.

## By Target

Notably, it is not necessarily true that parcellations with a higher number of parcels will always perform better.
For example, comparing between randomly generated parcellations and existing literature based parcellations
revealed consistently better performance for existing parcellations. This could suggest that, on average,
the existing parcellations map better onto meaningful neuro-anatomy relative to random parcellations of similar size.
Different phenotypes of interest also vary in how much they follow the observed scaling relationship.
We also found an interesting increase in spread of mean ranks as the number of parcels grew,
where not only the mean rank increased but also the inter quartile range at each size increased.
This behavior is likely a result of the distributed and complex brain-based nature of the phenotypes studied,
where different targets may have different optimal resolutions.
That said, the pattern in the average case remains clear and, we argue, is still
meaningful despite recognizing that variation exists across possible phenotypes. 


