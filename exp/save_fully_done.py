''' 
This file can be run occasionally, it is used to cut down on the time
it takes to check if results are full done or just still running.
'''

import numpy as np
import os
from joblib import Parallel, delayed
import pickle as pkl

from config import results_dr, fixed_done_loc

def check_if_fully_done(result_loc):
    '''Check if fully done, i.e., not in progress, not time limit.'''

    try:
        r = np.load(result_loc)
        if len(r) > 1:
            return result_loc
    except:
        return None

def save_fully_done():
    '''Utility to save configurations which are fully complete.'''
    
    # Get as set of locations
    results = os.listdir(results_dr)
    locs = set([os.path.join(results_dr, result) for result in results])

    # Get only locations unsure if done
    done_paths = Parallel(n_jobs=8, prefer='threads')(
        delayed(check_if_fully_done)(loc) for loc in locs)
    all_done_paths = set(done_paths)
    
    # Print #
    print('Saved Fully Done:', len(all_done_paths))
    
    # Save to fixed done location
    with open(fixed_done_loc, 'wb') as f:
        pkl.dump(all_done_paths, f)

def main():
    save_fully_done()

if __name__ == '__main__':
    main()