---
layout: default
title: Target Variables
description: Information of the different target variables used.
---

A collection of 45 target phenotypic variables (23 binary and 22 continuous), used to gauge predictive performance,
was sourced from the second ABCD Study release. Variables were sourced directly from
the rds file made available by the DAIRC (specifically on a version of the rds file saved as a csv).
All collected variables, both target and brain, are from the baseline time point on the study.
Best efforts were made to source a list of representative, diverse and predictive variables.
Towards this effort, a larger list of variables was originally screened on a subset of the data (n=2000)
to avoid including variables not at all predictive from sMRI measures.


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
                                                                             ||[months-breast-fed](./target_variables#months-breast-fed)|

























Note: To see more information on a specific target variable click the name above.

Extra pre-processing beyond done by the DEAP team, and the creation of the targets.csv is conducted in the script setup/process_targets.py