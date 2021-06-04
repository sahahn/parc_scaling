---
layout: default
title: Variables Used
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
[Standing Height (inches)](./target_variables#standing-height-inches)|
[Waist Circumference (inches)](./target_variables#waist-circumference-inches)|               
[Measured Weight (lbs)](./target_variables#measured-weight-lbs)|
[CBCL RuleBreak Syndrome Scale](./target_variables#cbcl-rulebreak-syndrome-scale)|                   
[Parent Age (yrs)](./target_variables#parent-age-yrs)|                      
[Motor Development](./target_variables#motor-development)|                      
[Birth Weight (lbs)](./target_variables#birth-weight-lbs)|                               
[Age (months)](./target_variables#age-months)|                                        
[Little Man Test Score](./target_variables#little-man-test-score)|                                
[MACVS Religion Subscale](./target_variables#macvs-religion-subscale)|                             
[Neighborhood Safety](./target_variables#neighborhood-safety)|                               
[NeuroCog PCA1 (general ability)](./target_variables#neurocog-pca1-general-ability)|                   
[NeuroCog PCA2 (executive function)](./target_variables#neurocog-pca2-executive function)|
[NeuroCog PCA3 (learning / memory)](./target_variables#neurocog-pca3-learning-memory)|
[NIH Card Sort Test](./target_variables#nih-card-sort-test)|
[NIH List Sorting Working Memory Test](./target_variables#nih-list-sorting-working-memory-test)|
[NIH Comparison Processing Speed Test](./target_variables#nih-comparison-processing-speed-test)|
[NIH Picture Vocabulary Test](./target_variables#nih-picture-vocabulary-test)|
[NIH Oral Reading Recognition Test](./target_variables#nih-oral-reading-recognition-test)|
[WISC Matrix Reasoning Score](./target_variables#wisc-matrix-reasoning-score)|
[Summed Performance Sports Activity](./target_variables#summed-performance-sports-activity)|
[Summed Team Sports Activity](./target_variables#summed-team-sports-activity)|

Note: To see more information on a specific target variable click the name above.

Extra pre-processing beyond done by the DEAP team, and the creation of the targets.csv is conducted in the script setup/process_targets.py