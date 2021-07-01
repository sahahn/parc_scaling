---
layout: default
title: Target Variables
description: Information of the different target variables used.
---

# Target Variables

A collection of 45 target phenotypic variables (23 binary and 22 continuous), used to gauge predictive performance,
was sourced from the second [ABCD Study](https://abcdstudy.org/) release. Variables were sourced directly from
the rds file made available by the DAIRC (specifically on a version of the rds file saved as a csv,
See: [github link](https://github.com/ABCD-STUDY/analysis-nda) and [data repository](https://nda.nih.gov/abcd).
All collected variables, both target and brain, are from the baseline time point on the study.
Best efforts were made to source a list of representative, diverse and [predictive](./variables#is-predictive) variables.
Extra pre-processing beyond done by the DEAP team, and the creation of the targets.csv is conducted in the script [setup/process_targets.py](https://github.com/sahahn/parc_scaling/blob/main/setup/process_targets.py)

All target variables used in the final project are listed below with clickable links to a more detailed description of each measure. See also [distribution info for each target](./variables#targets-stats).

| Continuous Variables                  | Binary Variables                            |
|:--------------------------------------|:--------------------------------------------|
[Standing Height (inches)](./target_variables#standing-height-inches)|[Speaks Non-English Language](./target_variables#speaks-non-english-language)|
[Waist Circumference (inches)](./target_variables#waist-circumference-inches)|[Thought Problems ASR Syndrome Scale](./target_variables#thought-problems-asr-syndrome-scale)| 
[Measured Weight (lbs)](./target_variables#measured-weight-lbs)|[CBCL Aggressive Syndrome Scale](./target_variables#cbcl-aggressive-syndrome-scale)|
[CBCL RuleBreak Syndrome Scale](./target_variables#cbcl-rulebreak-syndrome-scale)|[Incubator Days](./target_variables#incubator-days)|                   
[Parent Age (yrs)](./target_variables#parent-age-yrs)|[Born Premature](./target_variables#born-premature)                  
[Motor Development](./target_variables#motor-development)|[Has Twin](./target_variables#has-twin)|                      
[Birth Weight (lbs)](./target_variables#birth-weight-lbs)|[Planned Pregnancy](./target_variables#planned-pregnancy)|                               
[Age (months)](./target_variables#age-months)|[Distress At Birth](./target_variables#distress-at-birth)|                                        
[Little Man Test Score](./target_variables#little-man-test-score)|[Mother Pregnancy Problems](./target_variables#mother-pregnancy-problems)|                                
[MACVS Religion Subscale](./target_variables#macvs-religion-subscale)|[Any Alcohol](./target_variables#any-alcohol)|                             
[Neighborhood Safety](./target_variables#neighborhood-safety)|[Any Marijuana](./target_variables#any-marijuana)|                               
[NeuroCog PCA1 (general ability)](./target_variables#neurocog-pca1-general-ability)|[KSADS OCD Composite](./target_variables#ksads-ocd-composite)|                   
[NeuroCog PCA2 (executive function)](./target_variables#neurocog-pca2-executive-function)|[KSADS ADHD Composite](./target_variables#ksads-adhd-composite)|
[NeuroCog PCA3 (learning / memory)](./target_variables#neurocog-pca3-learning-memory)|[KSADS Bipolar Composite](./target_variables#ksads-bipolar-composite)|
[NIH Card Sort Test](./target_variables#nih-card-sort-test)|[Mental Health Services](./target_variables#mental-health-services)|
[NIH List Sorting Working Memory Test](./target_variables#nih-list-sorting-working-memory-test)|[Detentions / Suspensions](./target_variables#detentions-suspensions)|
[NIH Comparison Processing Speed Test](./target_variables#nih-comparison-processing-speed-test)|[Parents Married](./target_variables#parents-married)|
[NIH Picture Vocabulary Test](./target_variables#nih-picture-vocabulary-test)|[Prodromal Psychosis Score](./target_variables#prodromal-psychosis-score)|
[NIH Oral Reading Recognition Test](./target_variables#nih-oral-reading-recognition-test)|[Screen Time Week (hrs)](./target_variables#screen-time-week)|
[WISC Matrix Reasoning Score](./target_variables#wisc-matrix-reasoning-score)|[Screen Time Weekend (hrs)](./target_variables#screen-time-weekend)|
[Summed Performance Sports Activity](./target_variables#summed-performance-sports-activity)|[Sex at Birth](./target_variables#sex-at-birth)|
[Summed Team Sports Activity](./target_variables#summed-team-sports-activity)|[Sleep Disturbance Scale](./target_variables#sleep-disturbance-scale)|
||[Months Breast Fed](./target_variables#months-breast-fed)|


## Is Predictive

In order to establish if potential target variables were predictive or not, we conducted a front-end test on a subset of data.
First a larger list of possible representative variables was sourced from
[Recalibrating expectations about effect size: A multi-method survey of effect sizes in the ABCD study](https://psyarxiv.com/tn9u4/).
A subset of around 2000 participants was then identified as participants with no missing values across all possible target variables.
Next, the Destrieux FreeSurfer extracted ROIs were used used as input features within a 5-fold cross validation framework to try and
predict out of sample each potential variable. A ridge regression model with nested random choice over 32 values of regularization,
along with front-end robust input scaling was used as the predictive ML pipeline (implemented and evaluated with [BPt](https://github.com/sahahn/BPt)).
Regression models with R2 as the metrics of interest were used for continuous variables, ROC AUC for
binary variables and matthews correlation coef. for categorical variables
(these types were auto-detected by [BPt](https://github.com/sahahn/BPt)).
Within this framework we then established variables as 'predictive' only if they had a
performance metric > than the null for that metric + the standard deviation
across five folds (e.g., for R2 needs an R2 > R2 std, but for ROC AUC needs ROC AUC > .5 + ROC AUC std). 


## Why Threshold

A number of the binary variables listed above were not originally binary variables, and instead were converted to binary
variables through a static threshold. This is often considered a poor statistical practice, so why did we do it in this context?
First, thresholding variables in this way while perhaps not best practice, does happen frequently in the literature, we therefore
wanted to mimic actually used practices in this sense. Secondly, we wanted to try and ensure that the number of continuous variables and
binary variables where roughly equal. Lastly, in a number of cases the continuous version of the variable was not at all predictive, but 
the binarized version was (likely due to the highly skewed nature of these variables true underlying distribution).

## Targets Stats

### Continuous

{% include float_table.html %}

### Binary

{% include binary_table.html %}