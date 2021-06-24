---
layout: default
---

# Performance Optimizations

These expiriments were extremely computationally intensive to run, thus requiring a number of optimizations. Even just the [base experiment](./index#base-experiment-setup) required running 148,500 (220 parcellations * 45 targets * 3 pipelines * 5 evaluation folds) combinations! Which isn't even considering the [multiple parcellation strategies](index.md#multiple-parcellation-strategies) or that each of the pipelines hyper-parameter searches required training 180 different models...

The main overarching optimization / just thing that even made this at all possible was that the [Vermont Advanced Computing Core](https://www.uvm.edu/vacc) was used to run all of the expiriments, which is a supercomputer. Even so, there are a number of other key / interesting optimizations
made. This page will discuss some of the optimizations we made that allowed us to actually finish these expiriments / waste less resources.

## Flexible Submission System

At first the idea of submitting jobs seems relatively easy, as essentially there are just a number of fixed configurations to run. We just need to run the `submit.py` file with all the choices of parcellation, model and target. Easy, just submit with 3 nested loops and done... except it turns out it isn't nearly that simple. 

The most fundamental problem relates to the different [computational resources](./trade_offs#runtime) required by each combination. As it turns out, all three of the parameters of interest end up changing the resources needed, and all in different ways. The new problem we end up with is then how do we submit all of these different combinations, some of which can be run with a single core and a GB of memory in 10 minutes, and some of which will take 30 hours and 20+ GB just to run a single of the 5-folds?

The other points of interest when running these expiriments were runtime, that is to say getting results ASAP, and using as little resources as possible, as the cluster is a shared resource / using more resources hurts priority queue scores. Lastly, we were also interested in a system which required little to no manual intervention or babysitting.

The solution we built is based off of a randomized submission system. The core idea is that when a SLURM job is submitted, the first thing that job does is select a set of parameters (target, pipeline and parcellation) from a pool of options. This pool of options by default is just all of the remaining not finished options, but in order to add flexibility to different runtime consideration can be through passed input arguments set when submitting the job be used to restrict the pool of options in different ways (e.g., to just a specific pipeline).

This base randomized submission systems has a few really nice traits: 

1. An arbitrary number of SLURM jobs can be submitted at any given time. Given that the cluster this was run on is shared by a number of other users, this was especially helpful as it let us submit large numbers of jobs during low usage times, and fewer jobs during periods of high use.
   
2. The system is flexible to failure. This is actually really important as ahead of time it is hard to know which configurations will fail. When a certain configuration fails though, it will be saved to an errors log and then just re-added to the pool of available jobs. In practice this means that without knowing ahead of time which jobs will fail, we could submit a first pass with a large number of low resource jobs. Then just a second pass with fewer high resource jobs that will end up processing only the ones that failed before as they will be all that are left unfinished. The key piece here is that we do not need to manually go in and check oh this specific job failed, then manually re-submit that job, etc... etc... instead we just continue to specify higher resource jobs.

Another aspect of the submission system which proved invaluable was a flag for certain parcellations with higher numbers of parcels. In this case these parcellation due to high numbers of input features would not be able to complete their 5-fold evaluation within a single 30 hour normal job. To solve this, we specified that these flagged parcellations would be submitted in an even more fine grained method, by-fold. These configurations were therefore added to the pool of options as not just choice of parcellation, pipeline and target but fold, and results saved for each fold by itself. This optimization proved sufficient for allowing us to run even very intensive expiriments, like parcellations with 6,000 parcels, using the same 30 hour default jobs. Likewise, using the flag method we were able to still save on the number of submitted jobs by still evaluating all five folds in one job for faster combinations of parameters!

## Caching

- Caching applying parcellation
- Extensive caching and re-use during multiple parcellation exp.

## Parallel Computing

It is common within ML implementations to be able to multi-process certain processes. This project was no exception, as we utilized heavily multi-processing (beyond the use of the cluster to submit multiple evaluation jobs at once) to parallelize primarily the hyper-parameter search within specific evaluation jobs.

- Experiments with different parallel computing strategies, including dask, and finally settling on joblib based solution.

## Other

- SVM hyper-parameter trick. 