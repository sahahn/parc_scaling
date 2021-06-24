# Performance Scaling for Structural MRI Surface Parcellations: A Machine Learning Analysis in the ABCD Study

<p align="center">
  <img width="800" src="https://raw.githubusercontent.com/sahahn/parc_scaling/master/analyze/Figures/Figure1.png">
</p>

This github repository contains READMEs dedicated primarily to explaining the actual usage and structure of this project's code - a separate dedicated project website can be found at https://sahahn.github.io/parc_scaling/ which acts as an online supplementary materials for the paper.

### Directory structure

This project is setup with a few different directories, which if necessary contain their own more detailed READMEs.

- `analyze/`

  This folder contains the code for processing, analyzing and plotting the results.

- `data/`

  This folder stores the processed data as generated from setup.

- `docs/`

  This include the markdown pages for the [project website](https://sahahn.github.io/parc_scaling/).

- `exp/`
  
  This folder includes all of the code used to perform the ML expiriments.

- `extra/`
  
  This folder contains various misc. notebooks for making brain figures and other random side-analyses. 

- [extra_random_parcels/](extra_random_parcels/)
  
  This folder is where the random parcellations used for the multiple parcellation strategies are stored. This folder is created and filled by a script in `setup/`.

- [parcels/](parcels/)
  
  This folder contains all of the processed and numpy saved versions of main parcellations
  used in this project.

- `raw/`

  This folder contains all of the raw data, parcellations and input data etc..., used in the project. See [raw/README.md](raw/README.md) for mo

- setup/

In general those starting with capital letters, (setup/, exp/, analyze/) contain code used to run different steps, with other directories used to store data or parcellations, e.g. (data/, parcels/, ect...).


<p align="center">
  <img width="600" src="https://raw.githubusercontent.com/sahahn/parc_scaling/master/data/t32_logo.png">
</p>