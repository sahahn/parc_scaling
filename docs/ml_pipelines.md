---
layout: default
title: ML Pipelines
description: Information of the different ML Pipelines used.
---

# ML Pipelines

The python library [BPt](https://github.com/sahahn/BPt) was used to implement three ML pipelines of interest.
Each pipeline has both a classifier and regressor variant, and were chosen in order to cover a representative sample of different popular and predictive ML strategies. These also include as built in a number of [performance optimizations](./optimizations.html) we made.

All ML pipelines consist of the same initial pieces, differing only on choice of base estimator. The first piece of all pipelines
is a [Loader](https://sahahn.github.io/BPt/reference/api/BPt.Loader.html#BPt.Loader),
which is responsible for extracting ROIs according to a specified surface parcellation, and then concatenating the features together. See
the section below specifically dedicated to Loaders.
The next shared piece is a [Scaler](https://sahahn.github.io/BPt/reference/api/BPt.Scaler.html), specifically a
[robust scaler](https://sahahn.github.io/BPt/options/pipeline_options/scalers.html#robust)
where each feature is standardized by first removing the median and then scaling according to the 5th and 95th percentiles of that features distribution.

Lastly, these features are used as input for one of three base estimator components, which are listed below:

#### Elastic-Net
The base model within the pipeline under this configuration is a logistic or linear regression with elastic-net penalty available from
[scikit-learn](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.ElasticNet.html).
A nested [random](https://sahahn.github.io/BPt/options/search_type_options/random_search.html)
[hyper-parameter search](https://sahahn.github.io/BPt/reference/api/BPt.ParamSearch.html) over 60 combinations is evaluated through
nested 3-fold [CV](https://sahahn.github.io/BPt/reference/api/BPt.CV.html#BPt.CV) to select the strength
of regularization applied as well as the ratio between
[l1 and l2 regularization](https://medium.com/analytics-vidhya/l1-vs-l2-regularization-which-is-better-d01068e6658c).

BPt Code:

~~~ python

    from BPt import CVStrategy, CV, ParamSearch, Model

    cv_strat = CVStrategy(groups='rel_family_id')

    base_param_search =\
        ParamSearch(search_type='RandomSearch',
                    n_iter=60,
                    cv=CV(splits=3, n_repeats=1, cv_strategy=cv_strat))

    model = Model('elastic',
                  params=1,
                  param_search=base_param_search,
                  tol=1e-3,
                  max_iter=1000)

~~~

In the code above, params=1 selects a default distribution of hyper-parameters from [BPt](https://github.com/sahahn/BPt), specifically
the [binary option](https://sahahn.github.io/BPt/options/pipeline_options/models.html#elastic-net-logistic) and
[regression option](https://sahahn.github.io/BPt/options/pipeline_options/models.html#elastic-net-regressor).

#### SVM
The base model within the pipeline under this configuration is a [Support Vector Machine (SVM)](https://scikit-learn.org/stable/modules/svm.html)
classifier or regressor with [radial basis function kernel](https://scikit-learn.org/stable/modules/svm.html#svm-kernels).
A front end [univariate feature selection](https://scikit-learn.org/stable/modules/feature_selection.html#univariate-feature-selection)
procedure was further added to this pipeline configuration (based on the
ANOVA f-value between a feature and the target variable). A nested [random](https://sahahn.github.io/BPt/options/search_type_options/random_search.html)
[hyper-parameter search](https://sahahn.github.io/BPt/reference/api/BPt.ParamSearch.html) over
60 combinations is then evaluated through nested 3-fold [CV](https://sahahn.github.io/BPt/reference/api/BPt.CV.html#BPt.CV)
in order to select the SVM’s strength of regularization and kernel coefficient as well as the percent of features to keep in the
front-end feature selector. All three hyper-parameters are optimized at the same time.

BPt Code:

~~~ python

    from BPt import CVStrategy, CV, ParamSearch, Model

    cv_strat = CVStrategy(groups='rel_family_id')

    base_param_search =\
        ParamSearch(search_type='RandomSearch',
                    n_iter=60,
                    cv=CV(splits=3, n_repeats=1, cv_strategy=cv_strat),
                    search_only_params={'svm classifier__probability': False})

    feat_selectors =\
        [FeatSelector('variance threshold'),
         FeatSelector('univariate selection', params=2)]

        
    base_model = Model('svm',
                        params=1,
                        cache_size=1500)

    nested_svm_pipe = Pipeline(steps=feat_selectors + [base_model],
                               param_search=base_param_search)

    model = Model(nested_svm_pipe)

~~~


In the code above, params=1 within the svm model selects a default distribution of hyper-parameters from [BPt](https://github.com/sahahn/BPt), specifically
the [binary option](https://sahahn.github.io/BPt/options/pipeline_options/models.html#svm-classifier) and
[regression option](https://sahahn.github.io/BPt/options/pipeline_options/models.html#svm-regressor). Likewise params=2 for the univariate
feature selector selects both a [binary option](https://sahahn.github.io/BPt/options/pipeline_options/selectors.html#univariate-selection-c) and
[regression option](https://sahahn.github.io/BPt/options/pipeline_options/selectors.html#univariate-selection-r) as well.

#### LGBM
The base model optimized is an [extreme gradient boosted tree](https://blog.exploratory.io/introduction-to-extreme-gradient-boosting-in-exploratory-7bbec554ac7)
based classifier and regressor from the [Light Gradient Boosting Machine (LGBM)](https://lightgbm.readthedocs.io/en/latest/) package.
The tuned hyper-parameters for this model included the type of boosting, the number of estimators, different tree sampling parameters, and regularization parameters. Given the high number of hyper-parameters to tune, 9, in contrast to the other base models, we employed a two point [differential evolution](https://en.wikipedia.org/wiki/Differential_evolution)
based [hyper-parameter search](https://sahahn.github.io/BPt/reference/api/BPt.ParamSearch.html) strategy implemented through the python library 
[Nevergrad](https://facebookresearch.github.io/nevergrad/). The search was run for 180 iterations, where each set of parameters is evaluated with a single 25% nested validation split.

BPt Code

~~~ python

    from BPt import CVStrategy, CV, ParamSearch, Model

    cv_strat = CVStrategy(groups='rel_family_id')
    p_cv = CV(splits=.25, n_repeats=1, cv_strategy=cv_strat)
    
    lgbm_param_search = ParamSearch(search_type='TwoPointsDE',
                                    n_iter=180,
                                    cv=p_cv)

    model = Model('light gbm',
                  params=1,
                  param_search=lgbm_param_search)

~~~

In the code above, params=1 selects a default distribution of hyper-parameters from [BPt](https://github.com/sahahn/BPt), specifically
the [binary option](https://sahahn.github.io/BPt/options/pipeline_options/models.html#light-gbm-classifier) and
[regression option](https://sahahn.github.io/BPt/options/pipeline_options/models.html#light-gbm-regressor).

### Source code

These pipelines are implemented in [exp/models.py](https://github.com/sahahn/parc_scaling/blob/main/exp/models.py)

### Loaders

A key piece of the different ML Pipelines are the ability to go from full surface level data to reduce dimensionality parcellated averages. This is accomplished through one of two different surface designed Loaders as currently implemented through the neurotools package (https://github.com/sahahn/neurotools), which we maintain. If a parcellation is static, a ‘SurfLabels’ object will be used, whereas if probabilistic, a different ‘SurfMaps’ object will be used.

In the case of the SurfLabels object, the dimensionality reduction is performed primarily as an averaging per separate unique ROI. The SurfMaps object on the other hand is designed to use either one of two different strategies for performing the dimensionality reduction. This is due to the fact that probabilistic based surface parcellations can either be made up of a set of maps that are more like weights (i.e., all positive values) or in a more complex case represent different positive and negative values. We therefore support with the SurfMaps object two different strategies, either set each region's value to the weighted average of each map, or calculate the least squares solution to the linear matrix equation between the data and the set of maps. Each method has their trade-offs, for example the weighted average is more simple to conceptualize as well as can be calculated faster, but it can only be done when the underlying maps are all positive and you may not compute the inverse weightings. The least squares strategy on the other takes longer, but can work when the underlying maps contain both positives and negatives and allow for inverse transformations. That said, based on internal testing, both strategies yield very similar downstream performance, so as a result in this project we employed the weighted average when weights were all positive and the least squares strategy otherwise.  

