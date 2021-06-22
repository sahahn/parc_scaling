import os
import numpy as np

# Get helpers from Exp directory
import sys
sys.path.append("../exp/")
from helpers import get_ensemble_options

from datetime import timedelta

def get_adj_size(parcel_str, grid=False):

    n_parcels = int(parcel_str.split('_')[3])
    parcel_size = parcel_str.split('_')[2]

    # If parcel size is a range
    if '-' in parcel_size:

        min_size = int(parcel_size.split('-')[0])
        max_size = int(parcel_size.split('-')[1])
        
        # In case of grid, lets go with max size... ?
        if grid:
            return max_size

        # Generate sizes as points between either end,
        sizes = np.linspace(min_size, max_size, n_parcels).astype('int')
        return np.sum(sizes)
    
    # If fixed just multiply size by base size
    else:
        base_sz = int(parcel_size)

        if grid:
            return base_sz

        return base_sz * n_parcels


def get_parc_sizes(parc_dr='../parcels',
                   base=False,
                   ico=False,
                   random=False,
                   fs=False,
                   stacked=False,
                   voted=False,
                   grid=False,
                   everything=False,
                   size_min=None,
                   size_max=None):

    if everything:
        base = True
        ico = True
        random = True
        fs = True
        stacked = True
        voted = True
        grid = True

    parc_sizes = {}
    
    # Get list of all parcels
    all_parcels = os.listdir(parc_dr)
    parcels = []

    for p in all_parcels:

        if p.startswith('random_'):
            if random:
                parcels.append(p)
        elif p.startswith('icosahedron'):
            if ico:
                parcels.append(p)
        else:
            if base:
                parcels.append(p)

    # Add all requested parcels
    for p in parcels:

        name = p.replace('.npy', '')
        parc = np.load(os.path.join(parc_dr, p))
        
        if len(parc.shape) == 2:
            sz = parc.shape[1]
        else:
            sz = len(np.unique(parc)) - 1
        
        parc_sizes[name] = sz
    
    # If extra freesurfer requested
    if fs:
        parc_sizes['freesurfer_destr'] = 150
        parc_sizes['freesurfer_desikan'] = 68
    
    # If different requested
    if stacked:
        for p in get_ensemble_options('stacked'):
            parc_sizes[p] = get_adj_size(p)

    if voted:
        for p in get_ensemble_options('voted'):
            parc_sizes[p] = get_adj_size(p)
    
    if grid:
        for p in get_ensemble_options('grid'):
            parc_sizes[p] = get_adj_size(p, grid=True)
    
    keys = list(parc_sizes)
    for key in keys:
        d = False
         
        # Enforce size min or max
        if size_min is not None:
            if parc_sizes[key] < size_min:
                d = True
        if size_max is not None:
            if parc_sizes[key] > size_max:
                d = True

        if d:
            del parc_sizes[key]

    return parc_sizes


def conv_t_delta(in_str):
    
    in_str = in_str.replace('Time Elapsed: ', '').strip()
    
    s = in_str.split(':')
    
    if len(s) == 3:
        return timedelta(hours=int(s[0]),
                         minutes=int(s[1]),
                         seconds=int(s[2]))
    else:
        print('Error with:', s)
        
def is_binary(target):
    
    target = target.rstrip()
    
    if target.endswith('_binary'):
        return True
    
    # Otherwise check exceptions
    binary = ['ksads_back_c_det_susp_p', 'married.bl',
              'accult_phenx_q2_p', 'devhx_5_twin_p',
              'sex_at_birth', 'devhx_6_pregnancy_planned_p',
              'devhx_12a_born_premature_p',
              'ksads_back_c_mh_sa_p']

    return target in binary

def get_p_type(parcel):
    
    if parcel.startswith('stacked_'):
        return 'stacked'
    elif parcel.startswith('voted'):
        return 'voted'
    elif parcel.startswith('grid'):
        return 'grid'
    
    return 'base'

def get_time_elapsed(txt, n_strip):
    
    te_ind = 'Time Elapsed: '
    time_elapsed = [conv_t_delta(l) for l in txt if l.startswith(te_ind)]
    
    full = None
    if len(n_strip) == 4:
        if len(time_elapsed) == 1:
            full = time_elapsed[0] * 5
    else:
        if len(time_elapsed) == 5:
            full = np.sum(time_elapsed)
            
    return full

def get_n_jobs(txt):
    
    n_jobs_line = txt[['n_jobs = ' in line for line in txt].index(True)]
    n_jobs = n_jobs_line.replace('n_jobs = ', '').rstrip()

    return int(n_jobs)

def extract_run_info(txt):

    run_ind = 'Running for:'
    ind = [run_ind in line for line in txt].index(True)
    return txt[ind].replace(run_ind, '').strip()

def extract(txt, parc_sizes, skip_svm=False):
    
    # If not a finished run
    if not 'Validation Scores\n' in txt:
        return None
    
    # Get base run info
    n_strip = extract_run_info(txt).split('---')
    parcel, model = n_strip[0], n_strip[1]
    is_b = is_binary(n_strip[2])
    
    # Skip SVM if skip SVM
    if skip_svm and model == 'SVM':
        return None

    # Set p_type by if ensemble
    p_type = get_p_type(parcel)
    
    # Get parcel size, if invalid skip
    try:
        size = parc_sizes[parcel]
    except KeyError:
        return None

    # Get time elapsed
    full = get_time_elapsed(txt, n_strip)
    
    # If not valid number of times
    # means didn't fully finish and skip this run
    if full is None:
        return None
    
    # Convert to seconds
    secs = full.total_seconds()
    
    # Extract n_jobs
    n_jobs = get_n_jobs(txt)
    
    # Get number of load saved
    n_load_saved = sum(['Loading from saved!' in line for line in txt])
    
    return model, size, is_b, secs, p_type, n_jobs, n_load_saved

def save_stats_summary(model, name):

    # Save html stats table
    html = '<html><body>' + model.summary().tables[0].as_html() + '<br>'
    html += model.summary().tables[1].as_html() + '</body></html>'

    with open('../docs/_includes/' + name + '.html', 'w') as f:
        f.write(html)

def save_results_table(r_df, name):
    
    r_df = r_df.rename({'Mean_Rank': 'Mean Rank', 'r2': 'R2',
                        'roc_auc': 'ROC AUC', 'full_name': 'Parcellation'}, axis=1)
    
    r_df = r_df[['Parcellation', 'Mean Rank', 'Size', 'R2', 'ROC AUC']]
    r_df = r_df.sort_values('Mean Rank')

    html = '<script src="https://www.kryogenix.org/code/browser/sorttable/sorttable.js"></script>'
    html += r_df.to_html(float_format="%.3f", classes=['sortable'],
                         index=False, justify='center')

    with open('../docs/_includes/' + name + '.html', 'w') as f:
        f.write(html)