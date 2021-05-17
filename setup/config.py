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
matlab_bin_loc = '/home/sage/Downloads/matlab/bin'
conv_script_loc = '/home/sage/data/CBIG/stable_projects/registration/Wu2017_RegistrationFusion/bin/standalone_scripts_for_MNI_fsaverage_projection/CBIG_RF_projectMNI2fsaverage.sh'
freesurfer_loc = '/home/sage/Downloads/freesurfer'