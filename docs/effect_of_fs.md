---
layout: default
title: Effects of Feature Selection
---

# How does front-end univariate feature selection influence scaling?

One reasonable question to ask when comparing the results of the SVM and Elastic-Net pipelines, for example, is to wonder if the SVM's better scaling (i.e., the Elastic-Net stop showing improvment to performance at a lower number of parcels relative to the SVM) is a result of the front-end feature selection built into the SVM See [ML Pipelines](./ml_pipelines.html).

## Elastic-Net FS

To answer this, we can compare the base Elastic-Net pipeline (see [Elastic-Net](./ml_pipelines#elastic-net)) to a modfied version, Elastic-Net FS (feature selection) where a front-end feature selection step is added, simmilar to how the SVM pipeline is setup. Specifically,

Elastic-Net FS BPt Code:

~~~ python

    from BPt import CVStrategy, CV, ParamSearch, Model

    cv_strat = CVStrategy(groups='rel_family_id')

    base_param_search =\
        ParamSearch(search_type='RandomSearch',
                    n_iter=60,
                    cv=CV(splits=3, n_repeats=1, cv_strategy=cv_strat))

    base_model = Model('elastic',
                        params=1,
                        tol=1e-3,
                        max_iter=1000)

    nested_elastic_pipe = Pipeline(steps=feat_selectors + [base_model],
                                   param_search=base_param_search)
 
    model = Model(nested_elastic_pipe)

~~~

## Elastic-Net vs. Elastic-Net FS (Intra-Pipeline)

We compare here the two pipeline in an intra-pipeline fashion, essentially comparing the patterns of scaling between the two pipelines. First, we consider an unthresholded version (i.e., without [first estimating the powerlaw region](./estimate_powerlaw.html) then truncating). This comparison is notably limited to only the parcellations from the [base results](./base_results.md). The statistical models fit are of the form: `log10(Mean_Rank) ~ log10(Size) + C(Pipeline)`.

![Intra No Threshold](https://raw.githubusercontent.com/sahahn/parc_scaling/master/analyze/Figures/intra_elastic_vs_fs_no_threshold.png)

{% include intra_elastic_vs_fs_no_threshold.html %}

It also may be worthwhile to consider the same version but only within the regions seperately estimated to be consistent with powerlaw scaling (See [Powerlaw Scaling](./estimate_powerlaw.html)).

![Intra Threshold](https://raw.githubusercontent.com/sahahn/parc_scaling/master/analyze/Figures/intra_elastic_vs_fs_threshold.png)

{% include intra_elastic_vs_fs_threshold.html %}

In both cases, regardless of thresholding, we find that scaling remains quite consistent with or without front-end scaling. This implies that the better scaling observed with the SVM results is not due to the impact of the front-end feature selection.


## Elastic-Net vs. Elastic-Net FS (Inter-Pipeline)

It is also useful to consider the choice between with front-end feature selection and without in the context of raw performance (i.e., maybe there are no scaling benefits, but is performance improved?). We apply a simmilar statistical model from before, but this time where Mean Rank is derived in an inter-pipeline fashion, formula: `log10(Mean_Rank) ~ log10(Size) + C(Pipeline)`.

![Inter](https://raw.githubusercontent.com/sahahn/parc_scaling/master/analyze/Figures/inter_elastic_vs_fs.png)

{% include inter_elastic_vs_fs.html %}

In this case we observe only a very slight, and just barely non signifigant increase in performance when the nested feature selection is added. In practice, it should not matter which version is used.
