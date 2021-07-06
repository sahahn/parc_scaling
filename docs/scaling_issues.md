---
layout: default
title: Scaling Issues
---

# Scaling Issues

One's first intuition when generating a composite measure of performance across multiple target variables, even if both
say use explained variance as the metric of interest, is to simply average them. In the case where these target variables
are on roughly simmilar scales, that is to say, both similarly predictive in the best and worst cases, this might not be a bad
choice. Consider on the other hand though when they are not on the same scale, for example let's say our target variables are
[Waist Circumference (inches)](./target_variables#waist-circumference-inches)
and [CBCL RuleBreak Syndrome Scale](./target_variables#cbcl-rulebreak-syndrome-scale),
which for the [Elastic-Net](./ml_pipelines#elastic-net) Pipeline
and with [Random Parcellations](./parcellations#random-parcellations)
scored:


| Parcellation                 | Waist Circumference (inches) Explained Variance | CBCL RuleBreak Syndrome Scale Explained Variance |
|:-----------------------------|:------------------------------------------------|:-------------------------------------------------|
|Random 1000 Parcels           | 0.094893                                        | 0.016451                                         |
|Random 10 Parcels             | 0.028499                                        | 0.007476                                         |


The mean explained variance in this case is 0.055672 for Random 1000 Parcels and 0.017988 for Random 100 Parcels.
The obvious problem is that the score from Waist Circumference (inches) contributes far
more to this average score than CBCL RuleBreak Syndrome Scale,
which introduces an unintended bias which says that performance
predicting Waist Circumference (inches) is more important. Instead, we are more interested in that
in this example the 1000 parcel solution does better than the 10 parcel solution in both cases (what we lose
in order of magnitude when comparing between only 2 parcellations we re-gain by comparing 100+ parcellations). This
issue of target variables having different scales of predictability is one of the main reasons we use
[Mean Rank](./results_intro#mean-rank) as the metric of performance within this project.
