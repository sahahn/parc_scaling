---
layout: default
---

# Trade-Offs

Ultimately, in performing neuroimaging based machine learning, maximizing performance will typically not be the only consideration. Performance importantly has trade-offs with two other potentially key areas, namely interpretability and computational resources. We will consider first the findings from the paper under the lens of influencing interpretability. A natural benefit inherent in some existing parcellations is their popularity and widespread usage, which means named regions can be easily compared to prior literature employing that same atlas. For other parcellations, random or existing, it may instead require back-projecting feature importances to vertex surface space and interpreting values in this space. Similarly, instead of back-projecting feature importances, the parcellation itself can be automatically compared with a well known parcellation and region names assigned as combinations of well known regions.

Choice of pipeline will also influence how easily feature importances can be obtained, for example the Elastic-Net has associated beta weights and LGBM based pipeline a few different, although imperfect, measures of built in feature importance. The SVM based model though, since it employs the nonlinear radial basis function kernel, does not compute any built in measures of feature importance. Instead, a model-agnostic method must be used in order to derive feature importances. While these methods have their own trade-offs, there is certainly a growing interest in developing approaches to explain the outputs from “black-box” models (Altmann 2010, Lundberg 2017, Poyiadzi 2020). Similar to choice of pipeline is if to ensemble over multiple parcellations, where if an ensemble method is used, then interpretation is generally made more complex. For the voting ensemble, feature importances from the sub-model can be simply averaged, whereas for the stacking based ensemble a weighted average, according to the stacking models beta weights, can be used. In both cases, model-agnostic measures can of course also be used, as if sub-models are made up of different combinations of estimators, then the previously mentioned strategies become difficult or impossible to implement. 

Highly relevant to the current work, is how the number of parcellations influences the amount of computational resources and time needed to perform ML. Specifically, as the number of parcels increases, the number of input features grows, thus incurring, depending on the ML algorithm used, sometimes substantial increases to runtime and memory requirements. For example, consider the runtime required to perform a 5-fold evaluation for a few different configurations of choice of model and parcellation (all performed on a cluster node with 8 cores and 8GB of RAM):

SVM, 2000 parcels: 15 hours
Elastic-Net, 2000 parcels: 1 hour
SVM, 200 parcels: 1.75 hours
Elastic-Net, 200 parcels: .25 hours

Notably these times were also influenced by a number of other factors including the target variable, if that variable was binary, the type of cluster node and other factors. These examples were chosen to be representative roughly of the average time, but for example another instance of Elastic-Net with 2000 parcels took ~20 hours. There are also upper limits of runtime complexity to consider, where for example we were unable to finish even a single of the 5 fold evaluations for the SVM pipeline on unparcellated vertex-wise data in under a week, despite employing a cluster a node with 4 cores and 256GB of memory. That said, if one were interested only in performing ML on vertex-wise data there are specially designed implementations of some algorithms which may be far more suitable for such high dimensional data. On the other hand, even if prioritizing performance, our current work shows that employing vertex-data directly may not even be necessary, as maximum performance (i.e., the end of the power law size scaling) can be reached with between 10^3 and 10^4 parcels. 

## References

- Altmann, A., Toloşi, L., Sander, O., & Lengauer, T. (2010). Permutation importance: a corrected feature importance measure. Bioinformatics, 26(10), 1340-1347.

- Lundberg, S. M., & Lee, S. I. (2017). A unified approach to interpreting model predictions. In Advances in neural information processing systems (pp. 4765-4774).

- Poyiadzi, R., Sokol, K., Santos-Rodriguez, R., De Bie, T., & Flach, P. (2020, February). FACE: feasible and actionable counterfactual explanations. In Proceedings of the AAAI/ACM Conference on AI, Ethics, and Society (pp. 344-350).
