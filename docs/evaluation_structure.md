---
layout: default
title: Evaluation Structure
---

# Evaluation Structure

![Outline](https://raw.githubusercontent.com/sahahn/parc_scaling/master/analyze/Figures/Figure1.png)

To evaluate a given target variable, parcellation, or machine learning strategy’s performance, we defined an explicit framework to compare different combinations of methods. We evaluated each combination of target variable, parcellation and ML pipeline with five-fold [cross validation](https://scikit-learn.org/stable/modules/cross_validation.html) using the full set of available participants. This evaluation strategy is well known as [K-Fold cross validation](https://machinelearningmastery.com/k-fold-cross-validation/).

- Each of the validation folds, including any nested parameter tuning folds, were conducted such that participants from the same family were preserved within the same training or testing fold. This consideration was made as the ABCD Study was specifically designed to [recruit a large number of siblings and twins](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6314286/).

- The 5-fold structure was kept constant and therefore comparable across all combinations of ML pipeline, target variable, and parcellation (including both the [base experiment](./index#base-experiment-setup) and [multiple parcellation experiment](./multiple_parcellations_setup.html)). In the case of missing target variables (see NaN Counts in [Target Stats](./variables#target-stats)), those participants with missing data were simply excluded from their respective training or validation fold (i.e., if missing from a training fold then just not included in training, if missing from a validation fold then not included in generating the validation metric).

- In principle while it may have been more reliable to perform multiple repeats of the five-fold evaluation, the additional computation would have proved intractable given the already considerable [runtime](./trade_offs#runtime) required for even a single 5-fold evaluation.