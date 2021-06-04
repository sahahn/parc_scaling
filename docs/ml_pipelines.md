---
layout: default
title: ML Pipelines
description: Information of the different ML Pipelines used.
---

We employ three base ML pipelines, each with classifier and regressor variants, as a representative sample of different popular and predictive ML strategies. All machine learning experiments are conducted with the python library BPt. Each pipeline is first composed of a loading component responsible for extracting ROIs according to the specified surface parcellation. The output from the loading step concatenates the extracted ROI values across each of the different surface values, generating a feature vector of length four times the number of parcels for each subject. Next, the ROI values are scaled using robust scaling, where each feature is standardized by first removing the median and then scaling according to the 5th and 95th percentiles of that features distribution. These features are then used as input to train a classifier or regressor under one of three different base configurations, these are:


#### Elastic-Net
The base model within the pipeline under this configuration is a logistic or linear regression with elastic-net penalty available from scikit-learn. A nested random hyper-parameter search over 60 combinations is evaluated through nested 3-fold CV to select the strength of regularization applied as well as the ratio between l1 and l2 regularization.

    param_search = Param_Search(search_type='RandomSearch', n_iter=60,
                                splits=3, n_repeats=1, cv=cv)

    model = Model('elastic', params=1,
                  param_search=param_search,
                  extra_params={'tol': 1e-3})

#### SVM
The base model within the pipeline under this configuration is a Support Vector Machine (SVM) classifier or regressor with radial basis function kernel available from scikit-learn. A front end univariate feature selection procedure was further added to this pipeline configuration (based on the ANOVA f-value between a feature and the target variable). A nested random hyper-parameter search over 60 combinations is then evaluated through nested 3-fold CV in order to select the SVM’s strength of regularization and kernel coefficient as well as the percent of features to keep in the front-end feature selector. All three hyper-parameters are optimized at the same time.

    param_search = Param_Search(search_type='RandomSearch', n_iter=60,
                                splits=3, n_repeats=1, cv=cv,
                                search_only_params={'svm classifier__probability': False})

    feat_selector =\
            [Feat_Selector('variance threshold'),
             Feat_Selector('univariate selection', params=2)]

    nested_svm_pipe =\
        Model_Pipeline(feat_selectors=feat_selector,
                       model=Model('svm', params=1, extra_params={'cache_size': 2000}),
                       param_search=param_search)

    model = Model(nested_svm_pipe)


#### LGBM
The base model optimized is an extreme gradient boosted tree based classifier and regressor from the Light Gradient Boosting Machine (LGBM) package. The tuned hyper-parameters for this model included the type of boosting, the number of estimators, different tree sampling parameters, and regularization parameters. Given the high number of hyper-parameters to tune, 9, in contrast to the other base models, we employed a two point differential evolution based hyper-parameter search strategy implemented through the python library Nevergrad. The search was run for 180 iterations, where each set of parameters is evaluated with a single 25% nested validation split.


    lgbm_param_search =\
            Param_Search(search_type='TwoPointsDE', n_iter=180,
                         splits=0.25, n_repeats=1, cv=cv)

    model = Model('light gbm', params=1, param_search=lgbm_param_search)