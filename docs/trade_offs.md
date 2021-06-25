---
layout: default
---

# Trade-Offs

Ultimately, in performing neuroimaging based machine learning, maximizing performance will typically not be the only consideration.
Performance importantly has trade-offs with two other potentially key areas, namely [interpretability](./trade_offs#interpretability) and [computational resources](./trade_offs#runtime).

## Interpretability

A natural benefit inherent in some existing parcellations is their popularity and widespread usage, which means named regions can be easily compared to prior literature employing that same atlas. For other parcellations, random or existing, it may instead require back-projecting feature importances
to vertex surface space and interpreting values in this space. Similarly, instead of back-projecting feature importances,
the parcellation itself can be automatically compared with a well known parcellation and
region names assigned as combinations of well known regions.

Choice of pipeline will also influence how easily feature importances can be obtained,
for example the Elastic-Net has associated beta weights and LGBM based pipeline a few different, although imperfect, measures of built in feature importance.
The SVM based model though, since it employs the nonlinear radial basis function kernel, does not compute any built in measures of feature importance.
Instead, a model-agnostic method must be used in order to derive feature importances. While these methods have their own trade-offs, there is certainly a growing interest in developing approaches to explain the outputs from “black-box” models ([Altmann 2010](https://academic.oup.com/bioinformatics/article/26/10/1340/193348), [Lundberg 2017](https://arxiv.org/abs/1705.07874), [Poyiadzi 2020](https://research-information.bris.ac.uk/ws/portalfiles/portal/221094080/aies2020cr.pdf)).

Similar to choice of pipeline is if to ensemble over multiple parcellations, where if an ensemble method is used, then interpretation is generally made more complex.
For the voting ensemble, feature importances from the sub-model can be simply averaged, whereas for the stacking based ensemble a weighted average,
according to the stacking models beta weights, can be used.
In both cases, model-agnostic measures can of course also be used, as if sub-models are made up of different combinations of estimators,
then the previously mentioned strategies become difficult or impossible to implement.

That said, within this project we were not interested directly in interpretability concerns, although important. 

## Runtime

The ML methods, atleast those used in this project, scale differently with respect to the number of input features.
This scaling is therefore influenced by the the scale of the parcellations used as those with more parcels
will produce more input feature and that will effect the computational resources needed to perform ML.
We will consider in this section the influence of different parameters on runtime, despite a number of [performance optimizations](./optimizations.html) we made.



### Upper Limit

There are also upper limits of runtime complexity to consider. We originally planned to run expiriments on the highest resolution data available, this is the vertex level data directly, but ultimately where unable to finish any of the expiriments (except the Elastic-Net based pipeline for regression targets only). The rest of the configurations, even running just a single of the 5 fold evaluations with up to 4 cores and up to 256GB of memory, were unable to complete within a week (the maximum time limit on the cluster) or failed due to memory constraints. 
The caveat here is that the algorithms and implementations we used were not necessarily designed for such high input data. If one were interested only in performing ML on vertex-wise data there are specially designed implementations of some algorithms which may be far more suitable. On the other hand, even if prioritizing performance, our current work shows that employing vertex-data directly may not even be necessary, as maximum performance (i.e., the end of the power law size scaling) can be reached with between 10^3 and 10^4 parcels. 

## References

- [Altmann, A., Toloşi, L., Sander, O., & Lengauer, T. (2010). Permutation importance: a corrected feature importance measure. Bioinformatics, 26(10), 1340-1347.](https://academic.oup.com/bioinformatics/article/26/10/1340/193348)

- [Lundberg, S. M., & Lee, S. I. (2017). A unified approach to interpreting model predictions. In Advances in neural information processing systems (pp. 4765-4774).](https://arxiv.org/abs/1705.07874)

- [Poyiadzi, R., Sokol, K., Santos-Rodriguez, R., De Bie, T., & Flach, P. (2020, February). FACE: feasible and actionable counterfactual explanations. In Proceedings of the AAAI/ACM Conference on AI, Ethics, and Society (pp. 344-350).](https://research-information.bris.ac.uk/ws/portalfiles/portal/221094080/aies2020cr.pdf)
