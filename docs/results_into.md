---
layout: default
title: Intro to Results
---

The measure of performance presented within with project is typically in terms of 'Mean Rank'. This measure can be
potentially confusing as it can change subtly from figure to figure. In the most simple case though, Mean Rank, is 
as the name suggests, just an average of an evaluated pipeline-parcellations pair's rank in contrast to others. For example
consider the highly simplified example below:

![simple intro figure](https://raw.githubusercontent.com/sahahn/Parcs_Project/master/data/intro_figure1.png)



In order to evaluate and compare across both different binary and regression metrics, as well as to address scaling issues between metrics
(e.g., sex is more predictive than ADHD composite score) we adopted mean rank as our performance metric of interest.
We first define rank based on computing the relative per-target ranking across considered parcellations
(or in some cases parcellation-pipeline combinations), where the parcellation result with the highest score would receive rank 1 (i.e., lower rank better).
This metric can notably change depending on the subset of included parcellations or parcellation-pipeline pairs which are compared.
Mean rank can also further refer to different aggregations of these base ranks, for example in Figure 2 and 5, an average rank is first
computed separately for each pipeline across all target ranks, then set as a final mean rank across pipeline averages.
Whereas for example in the bottom of Figure 3, mean rank is computed directly between pairs of parcellation-pipelines.