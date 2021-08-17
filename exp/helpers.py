import os
import numpy as np
import pandas as pd
import time
import random
from joblib import Parallel, delayed
import pickle as pkl

from config import (models, split_if, results_dr,
                    fixed_done_loc, targets_loc, parcel_dr,
                    ensemble_sizes, ensemble_n_choices, ensemble_n_repeats,
                    special_ensembles)

def check_if_done(result_loc):
    '''Check if a saved location is finished or not.'''

    try:
        r = np.load(result_loc)
    except ValueError:
        return result_loc
    except FileNotFoundError:
        return None

    # If done add
    if len(r) > 1:
        return result_loc

    # If started less than 30hr ago, treat as done
    elif time.time() - r < 108000:
        return result_loc

    # Everything else, treat as not done
    return None

def get_done():
    
    # Try to load fixed done
    try:
        with open(fixed_done_loc, 'rb') as f:
            fixed_done = pkl.load(f)
    except FileNotFoundError:
        fixed_done = set()
    except:
        fixed_done = set()

    # Check which jobs are done
    results = os.listdir(results_dr)
    locs = set([os.path.join(results_dr, result) for result in results])

    # Get only locations unsure if done - use multi-proc.
    to_check_locs = locs - fixed_done
    print(f'checking {len(to_check_locs)} for combos to run.', flush=True)

    done_paths = Parallel(n_jobs=8, prefer='threads')(
        delayed(check_if_done)(loc) for loc in to_check_locs)
    done_paths = set(done_paths)
    
    # Merge with fixed done
    all_done_paths = done_paths.union(fixed_done)
    all_done_paths = [loc.replace('.npy', '') for loc in all_done_paths if loc is not None]
    all_done_paths = set([loc.split('/')[-1] for loc in all_done_paths])

    return all_done_paths

def get_name(parcel, model, target, split=None):
    '''Get name of run based on parcel, model, target and split.'''

    name = parcel + '---' + model + '---' + target

    if split is not None:
        name += '---' + str(split)

    return name

def load_target_names():

    # Target names
    targets = list(pd.read_csv(targets_loc,
                               index_col='src_subject_id',
                               nrows=0))
    
    # Not a target, used to define group splitting behavior.
    targets.remove('rel_family_id') 

    return targets

def get_ensemble_options(prepend, add_special=True):

    parcels = []

    # First add the different combinations of random ensembles
    random_seeds = [str(i) for i in range(int(ensemble_n_repeats))]

    for s in ensemble_sizes:
        for n in ensemble_n_choices:
            for r in random_seeds:

                parcels += [prepend + '_random_' + s + '_' + n + '_' + r]

    # Then add the extra special combinations
    if add_special:
        for key in special_ensembles:
            parcels += [prepend + '_' + key]

    return parcels

def get_parcels(model_choices):
    '''Return a list of all parcels choices / strategies.'''

    # Start with all base parcels
    parcels = [p.replace('.npy', '') for p in os.listdir(parcel_dr)]

    # Add two freesurfer ROI options
    parcels += ['freesurfer_destr', 'freesurfer_desikan']
    
    # Skip base parcels if all in model choices
    if 'all' in model_choices:
        parcels = []

    # Add extra / ensemble - stacked, voted, grid
    for pre in ['grid', 'stacked', 'voted']:
        parcels += get_ensemble_options(pre)

    return parcels

def get_all_choices(parcels, model_choices, targets):
    '''Get all possible choices'''

    # Generate list of all valid choices
    all_choices = []

    for parcel in parcels:
        
        # If this parcel gets splits
        if any([parcel.startswith(s) for s in split_if]):
            needs_split = True
        else:
            needs_split = False

        for model in model_choices:
            for target in targets:

                # If doesn't need split, names are just one
                if not needs_split:
                    names = [get_name(parcel, model, target)]
                else:
                    names = [get_name(parcel, model, target, split=s) 
                             for s in range(5)]
                
                # Add to choices
                all_choices += names
    
    # Return as set
    return set(all_choices)

def get_choice(only=None):

    # Optional, if pass a list of only,
    # used passed instead of config variable models
    model_choices = models
    if only is not None:
        model_choices = only
    
    # Get all parcel options
    parcels = get_parcels(model_choices)

    # Load target names
    targets = load_target_names()

    # Ensure results directory is init'ed
    os.makedirs(results_dr, exist_ok=True)

    # Get set of finished result configurations
    done = get_done()

    # Generate list of all valid choices
    all_choices = get_all_choices(parcels, model_choices, targets)

    # Remove done from all choices
    all_choices = list(all_choices - done)
    print('Remaining Choices:', len(all_choices), flush=True)
    
    # If finished, return all None's
    if len(all_choices) == 0:
        return None

    # From all_choices, select one at random to return
    # this makes it less likely to submit two of the same job.
    name = random.choice(all_choices)
    
    # Unpack choice
    parcel = name.split('---')[0]
    model = name.split('---')[1]
    target = name.split('---')[2]

    # If needs split
    if len(name.split('---')) == 4:
        split = name.split('---')[3]
    else:
        split = None
    
    # Generate save loc for this configuration
    save_loc = os.path.join(results_dr, name + '.npy')
    
    # Set split as int
    try:
        split = int(split)
    except:
        split = None

    # Return this choice dictionary of arguments
    args = {'name': name,
            'save_loc': save_loc,
            'parcel': parcel,
            'model': model,
            'target': target,
            'split': split}

    return args