# exp/

This folder contains all of the code used in the main experiments of the paper. In order for this code to work, the steps outlines in setup must have first been completed.

### Files

- config.py
    
    This file contains information shared across different evaluation code in this directory, including file paths and which models to run. The location for different
    caching directories can also be specified here.

- evaluate.py

    This file contains the main evaluation loops code. The main function
    evaluate grabs the correct pipeline, loads the dataset and sets up
    the rest of the BPt 2.0 5-fold evaluation code. This function is also
    responsible for saving the output a completed run. It relies on
    auxillary file models.py to get the correct model pipeline and is called
    by submit.py.

- helpers.py

    This file contains primarily code related to generating the list of
    all possible experimental configurations and selecting a random valid
    choice to run (i.e., a choice that is not already completed and not currently running). 


### Computation

As these experiments are tremendously computationally expensive, they were run on the
University of Vermont's bluemoon super computing cluster (https://www.uvm.edu/vacc).
This cluster use's a SLURM submission system. Scripts dedicated to
submitting SLURM jobs are saved with the '.sh' suffix. Job's can also be run locally via running submission script 'submit.py'.

