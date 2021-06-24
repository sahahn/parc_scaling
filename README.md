# Performance Scaling for Structural MRI Surface Parcellations: A Machine Learning Analysis in the ABCD Study

<p align="center">
  <img width="800" src="https://raw.githubusercontent.com/sahahn/parc_scaling/master/analyze/Figures/Figure1.png">
</p>

This github repository contains READMEs dedicated primarily to explaining the actual usage and structure of this project's code - a separate dedicated project website can be found at https://sahahn.github.io/parc_scaling/ which acts as an online supplementary materials for the paper.

### Directory structure

This project is setup with a few different directories, which if necessary contain their own more detailed READMEs.

- [analyze](analyze/)/
  
  This folder contains the code for processing, analyzing and plotting the results.

- [config.json](config.json)

  This configuration file is used across the project to specify different key shared parameters.

- [data](data/)/

  This folder stores the processed data as generated from setup.

- [docs](docs/)/

  This include the markdown pages for the [project website](https://sahahn.github.io/parc_scaling/).

- [exp](exp/)/
  
  This folder includes all of the code used to perform the ML expiriments.
  See [exp/](exp/) README.md for more details.

- [extra](extra/)/
  
  This folder contains various misc. notebooks for making brain figures and other misc. side-analyses. 

- [extra_random_parcels](extra_random_parcels/)/
  
  This folder is where the random parcellations used for the multiple parcellation strategies are stored. This folder is created and filled by a script in [setup](setup/).

- [parcels](parcels/)/
  
  This folder contains all of the processed and numpy saved versions of main parcellations
  used in this project.

- [raw](raw/)/

  This folder contains all of the raw data, parcellations and input data etc..., used in the project. See [raw/](raw/) README.md for more details.

- [setup](setup/)/

  This folder contains the code used to setup the rest of the expiriments, including processing input data and parcellations for later ML. See [setup/](setup/) README.md for more details.


<p align="center">
  <img width="600" src="https://raw.githubusercontent.com/sahahn/parc_scaling/master/data/t32_logo.png">
</p>