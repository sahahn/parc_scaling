# Analyze

This sub-directory include the code and notebooks used to analyze the results from the main experiment as well as make plots and tables, etc... Included below is a brief description of what each included file is.

### Files

- [cluster_targets.ipynb](cluster_targets.ipynb)

    Notebook exploring how results change when limited to only
    different clusters of target variables.

- [extra_figures.ipynb](extra_figures.ipynb)
  
    Notebook dedicated to the creation of extra supplementary figures addressing
    some sub-questions of interest.

- [funcs.py](funcs.py)

    File including helper utilities for loading in raw saved numpy results into
    an organized form.

- [interactive_plots.ipynb](interactive_plots.ipynb)
  
    Notebook where the various interactive plots (created with plotly) are
    generated and saved as html files.

- [intro_to_results.ipynb](intro_to_results.ipynb)

    Notebook with an introduction on how to load and work with
    the raw results, for those interested in performing their own
    analyses on the raw results from this study.

- [make_paper_figures.ipynb](make_paper_figures.ipynb)

    Notebook responsible for generating the final, neat / pretty figures which will appear in the main manuscript for this work.

- [make_results_tables.ipynb](make_results_tables.ipynb)

    Notebook responsible for generating the HTML versions of different results
    tables featured throughout the online project documentation.

- [other_fs_models.ipynb](other_fs_models.ipynb)

    Notebook dedicated to answering the question on how a front-end feature
    selection scheme may or may not influence parcellation-performance scaling. Hint: it doesn't.

- [parse_runtime.ipynb](parse_runtime.ipynb)

    Notebook dedicated to exploring how runtime differed across different
    combinations of ML pipeline, ensemble strategy and parcellation.

- [plot_funcs.py](plot_funcs.py)

    The main file containing plotting functions used to generate and summarize
    results, used across most notebooks within this directory.


- [special_ensembles.ipynb ](special_ensembles.ipynb)

    Notebook dedicated to exploring a subset of special ensembles
    created from collections of existing parcellations.

- [stats.ipynb](stats.ipynb)

    Notebook containing the analyses code for all main statistical
    analyses included in the study, using library statsmodel.

- [targets_summary.ipynb](targets_summary.ipynb)

    Notebook where all of the target variables are automatically
    used to generated a summary .docx table.

