---
layout: default
---

# Optimizations

These expiriments were extremely computationally intensive to run, thus requiring a number of optimizations. 
The first, if it counts as one, is that the [Vermont Advanced Computing Core](https://www.uvm.edu/vacc) was used to
run all of the expiriments, which is a supercomputer. Even so, there are a number of other key / interesting optimizations
made. This page will discuss some of the optimizations we made that allowed us to actually finish these expiriments.

- Randomized Submission System
- Caching applying parcellation
- Extensive caching and re-use during multiple parcellation exp.
- SVM hyper-parameter trick
- Experiments with different parallel computing strategies, including dask, and finally settling on joblib based solution.