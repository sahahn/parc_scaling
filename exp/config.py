'''
This file is used to simply define a few constants used across different files.
'''
import os
import json

# Main project directory - shouldn't need to manually set, but could override
main_dr = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Load some values from global config json
with open(os.path.join(main_dr, 'config.json')) as f:
    config = json.load(f)

# The different models to use
models = config['models']

# The ensemble sizes
ensemble_sizes = config['ensemble_sizes']
ensemble_n_choices = config['ensemble_n_choices']
ensemble_n_repeats = config['ensemble_n_repeats']
ensemble_max_choice = max([int(c) for c in ensemble_n_choices])

# Which parcellations, start str stub, should be run as a job with only
# one fold, e.g., those that take a long time to complete.
split_if = ['stacked_', 'voted_', 'grid_',
            'random_2000_', 'random_3000_',
            'random_4000_', 'random_5000_',
            'icosahedron-1442_']

# Other directories based on main_dr
exp_dr = os.path.join(main_dr, 'exp')
results_dr = os.path.join(exp_dr, 'results')
fixed_done_loc = os.path.abspath(results_dr) + '_done.pkl'

data_dr = os.path.join(main_dr, 'data')
targets_loc = os.path.join(data_dr, 'targets.csv')

parcel_dr = os.path.join(main_dr, 'parcels')
extra_parcel_dr = os.path.join(main_dr, 'extra_random_parcels')

# These might want to change
cache_dr = os.path.join(exp_dr, 'cache')
cache_fit_dr = os.path.join(exp_dr, 'cache_fit')
