---
layout: default
---

## Project Introduction

Different parcellations and neuroimaging atlases are ubiquitous in neuroimaging, namely because they allow for a principled reduction of features (which has its own sleuth of benefits). This project focuses in particular on the question of choice of parcellation, in particular, how does choice of parcellation influence performance within a machine learning context.

[Background on Machine Learning for Neuroimaging](./ml_neuroimaging.html)

The base experiment conducted within this project was a systematic test of different pre-defined parcellations performance. The structure of the evaluation is shown below:

![Base Exp Structure](https://raw.githubusercontent.com/sahahn/Parcs_Project/master/analyze/Figures/Figure1.png)

- a). This study uses data from the ABCD Study release [NDA Collection 3165](https://collection3165.readthedocs.io/en/stable/).
Specifically, we concatenate structural MRI measures to use as input features (See [Input Data](./input_data.html) for more information).

- b). 

- c). Three different ML pipelines are used, each based on a different popular base estimator (See [ML Pipelines](./ml_pipelines.html))

- d). In total we employ 45 different phenotypic target variables (See [Target Variables](./variables.html)).

----




----



----

[Results](./results.html)

[Neuro-Imaging for ML Background and Motivation](./ml_neuroimaging.html)

[Random Parcellations](./random_parcellations.html)

[Performance Trade-Offs](./trade_offs.html)