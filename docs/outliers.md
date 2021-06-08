---
layout: default
title: Outliers
description: What outlier detection and removal was conducted.
---

# Outliers

All outlier processing was done with the python library [BPt](https://github.com/sahahn/BPt) and raw code can be
found at [setup/setup_dataset.py](https://github.com/sahahn/parc_scaling/blob/main/setup/setup_dataset.py)

## Input Data

First, in order for a participant to be included, they must have had no missing data across each input modality.
Automated outlier detection was then performed on the different [Input Data](./input_data.html) surfaces.
The goal of outlier detection in this context is to try and detect which subject's data were fully
corrupted for some reason, for example maybe a problem occurred during automated registration of the data.
To this end we employed a standard deviation based outlier detection method on each sMRI modality separately.

For myelin, thickness and sulcal depth, we first generated a single summary measure of the standard deviation of
each participants data across all vertex. This summary measure was then used to identify outliers, by marking outliers
as participants whose summary measure greater than or less than 10 standard deviations from the mean
(across all participants summary measures). For curvature, we found that a more procedure was necessary, where
we sequentially applied the 10 standard deviation outlier filtering to three different summary measures across vertex values
of curvature. These were the minimum value, the maximum value and then the standard deviation (same as the other three). This
sequential procedure allowed for removing strange outliers that existed at different extreme scales.
Any participant marked as an outlier for any of the modalities was dropped.

## Target Variables

We additionally checked to see if any of the target variables had extreme values. We employed standard deviation based
filtering to this end, dropping individually (setting to NaN) any values for continuous variables which were greater than or
less than 10 standard deviations from the mean. We did not perform any outlier filtering on binary variables except in setting
any values that were not one of the binary values to NaN.


