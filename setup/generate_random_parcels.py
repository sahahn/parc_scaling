from BPt.extensions import RandomParcellation
import numpy as np
import os

from config import (random_sizes, random_n_repeats, ensemble_sizes,
                    ensemble_n_choices, ensemble_n_repeats, ensemble_max_choice)
from helpers import load_geo, load_medial_wall

def gen_random(save_dr, sizes, rs_range):

    # Load geometry
    geo = load_geo(standard_mesh_loc='../raw/standard_mesh_atlases/')

    # Load medial wall mask
    medial_wall_mask =\
        load_medial_wall(annot_loc='../raw/fs_LR_32k_label/medialwall.annot')
    
    # Make sure save directory initialized
    os.makedirs(save_dr, exist_ok=True)
    
    # For each combination of size and random state
    for size in set(sizes):
        for random_state in range(rs_range):

            # Set save name
            save_name = os.path.join(save_dr, 'random_' + str(size) + '_' + str(random_state) + '.npy')

            # Only generate if it doesn't already exist
            # Though random state should ensure that it is the same anyway
            if not os.path.exists(save_name):
            
                # Generate this random parcel
                parc = RandomParcellation(geo, n_parcels=size,
                                          medial_wall_mask=medial_wall_mask,
                                          random_state=random_state).get_parc()

                # Save
                np.save(save_name, parc)
                print('Generated:', save_name, flush=True)

            else:
                print('Skip Generate:', save_name, flush=True)


# Base random sizes
gen_random('../parcels/', random_sizes, rs_range=random_n_repeats)

# Extra random parcel fixed sizes
fixed_sizes = [int(sz) for sz in ensemble_sizes if '-' not in sz]
gen_random('../extra_random_parcels/',fixed_sizes,
           rs_range=int(ensemble_max_choice * int(ensemble_n_repeats)))

# Process extra random parcels with ranges of sizes
sizes = []
range_sizes = [sz for sz in ensemble_sizes if '-' in sz]
for range_sz in range_sizes:
    low = int(range_sz.split('-')[0])
    hi = int(range_sz.split('-')[1])
    
    for choice in ensemble_n_choices:
        sizes += list(np.linspace(low, hi, int(choice)).astype('int'))

gen_random('../extra_random_parcels/', sizes,
           rs_range=int(ensemble_n_repeats))

