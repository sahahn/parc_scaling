import os
import json

# Main project directory - shouldn't need to manually set, but could override
main_dr = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Load some values from global config json
with open(os.path.join(main_dr, 'config.json')) as f:
    config = json.load(f)

# Number of random repeats for each sized
# random parcellation
random_sizes = config['random_sizes']
random_n_repeats = config['random_n_repeats']

# The ensemble info
ensemble_sizes = config['ensemble_sizes']
ensemble_n_choices = config['ensemble_n_choices']
ensemble_n_repeats = config['ensemble_n_repeats']
ensemble_max_choice = max([int(c) for c in ensemble_n_choices])

# Path's to extra libraries
matlab_bin_loc = config['matlab_bin_loc']
conv_script_loc = config['conv_script_loc']
freesurfer_loc = config['freesurfer_loc']