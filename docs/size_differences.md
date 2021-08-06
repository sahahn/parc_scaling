---
layout: default
title: Base Results Size Differences
description: Results by Parcellation Type
---

Notably in the first section of the [base results](./base_results.html), specifically with plotted
lines comparing randomly generated and existing.

![fits](https://raw.githubusercontent.com/sahahn/parc_scaling/master/analyze/Figures/base_results_fit1.png)

A follow up question one might have after looking at this plot is: Is there any potential problem with randomly generated parcellations extending
out beyond sizes 1000 whereas the existing based parcellations do not? The best way to answer this question is to compare the fits from the original
results to fits on a set of truncated results considering parcellations of size only up to 1000.

First the base results:

{% include base_results1.html %}

Truncated to 1000 results:

{% include base_results_1000_and_less.html %}

The conclusion after a bit of squinting is pretty clear, there is no real difference, the fits stay quite simmilar.