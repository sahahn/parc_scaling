# exp/

This folder contains all of the code used in the main experiments of the paper. In order for this code to work, the steps outlines in setup must have first been completed.

### Files

- [config.py](config.py)
    
    This file contains information shared across different evaluation code in this directory. It mostly takes
    values from the main config.json file and should not need to be edited.

- [evaluate.py](evaluate.py)

    This file contains the main evaluation loops code. The main function
    evaluate grabs the correct pipeline, loads the dataset and sets up
    the rest of the BPt 2.0+ 5-fold evaluation code. This function is also
    responsible for saving the output a completed run. It relies on
    auxillary file [models.py](models.py) to get the correct model pipeline and is called
    by [submit.py](submit.py).

- [helpers.py](helpers.py)

    This file contains primarily code related to generating the list of
    all possible experimental configurations and selecting a random valid
    choice to run (i.e., a choice that is not already completed and not currently running). 

- [models.py](models.py)

    This file contains the code defining the construction of the different ML Pipelines
    using BPt 2.0+ code. This include loading and caching components among others.

- [results.tar.gz](results.tar.gz)

    This is a compressed folder containing all of the results from the main experiment run in this directory. This results folder is accessed heavily in the analyze/ portion of the project code.

- [save_full_done.py](save_fully_done.py)

    This is a utility script which can be run at different intervals in order to mark
    certain combinations of results as finished, therefore allowing that new submissions
    do not need to repeatedly check to see if they are done.

- [submit.py](submit.py)

    This script is used to process input arguments for running different configurations of expiriments. This script if run directly will run an iteration of an experiment locally.

- [submit.sh](submit.sh)

    This is a SLURM submission script wrapper for submitting jobs. In practice
    it may be useful to generate multiple copies of this script with different parameters.
    This script also very well might need tweaks depending on the SLURM cluster being used.


### Computation

As these experiments are tremendously computationally expensive, they were run on the
University of Vermont's bluemoon super computing cluster (https://www.uvm.edu/vacc).
This cluster use's a SLURM submission system. Scripts dedicated to
submitting SLURM jobs are saved with the '.sh' suffix. Job's can also be run locally via running submission script [submit.py](submit.py) directly. 

