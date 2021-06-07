---
layout: default
title: Scaling Issues
---

One's first intuition when generating a composite measure of performance across multiple target variables, even if both
say use explained variance as the metric of interest, is to simply average them. In the case where these target variables
are on roughly simmilar scales, that is to say, both similarly predictive in the best and worst cases, this might not be a bad
choice. Consider on the other hand though when they are not on the same scale, for example let's say our target variables are
[Age (months)](./target_variables#age-months) and [CBCL RuleBreak Syndrome Scale](./target_variables#cbcl-rulebreak-syndrome-scale),
which for the [Elastic-Net](./ml_pipelines#elastic-net) Pipeline and [Random Parcellations](./parcellations#random-parcellations)