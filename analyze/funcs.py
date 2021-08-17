import os
import numpy as np

# Get helpers from exp directory
import sys
sys.path.append("../exp/")
from helpers import get_ensemble_options
from models import get_base_parcel_names

from datetime import timedelta


def get_multi_parcel_size(parcel, parc_dr):
    
    # Get names of component parcels
    base_parcels = get_base_parcel_names(parcel)
    
    # Get size of each base parcel
    base_parcel_sizes = [get_parcel_size(parc, parc_dr) for parc in base_parcels]

    # If grid, take max
    if parcel.startswith('grid_'):
        return max(base_parcel_sizes)

    # Otherwise, sum
    return sum(base_parcel_sizes)

def get_parcel_size(parcel, parc_dr):
    
    # Multiple parcellation cases
    if parcel.startswith('stacked_') or parcel.startswith('voted_') or parcel.startswith('grid_'):
        return get_multi_parcel_size(parcel, parc_dr)
    
    # Random parcel case (can know size from name, no need to load)
    if parcel.startswith('random_'):
        return int(parcel.split('_')[1])
    
    # Freesurfer cases
    if parcel == 'freesurfer_destr':
        return 150
    if parcel == 'freesurfer_desikan':
        return 68

    # Otherwise determine size by loading and checking unique number of parcels

    # Load parcel to check size
    parc = np.load(os.path.join(parc_dr, parcel + '.npy'))
    
    # If probabilistic
    if len(parc.shape) == 2:
        sz = parc.shape[1]

    # If static, minus 1 for parc marking empty / 0
    else:
        sz = len(np.unique(parc)) - 1

    return sz


def get_parc_sizes(parc_dr='../parcels',
                   base=False,
                   ico=False,
                   random=False,
                   fs=False,
                   stacked=False,
                   voted=False,
                   grid=False,
                   add_special=False,
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
        add_special = True

    # First fill list with all options based on passed options
    parcels = []
    
    # Base parcels are either random, ico or base existing
    all_parcels = [parc.replace('.npy', '') for parc in os.listdir(parc_dr)]
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

    # If extra freesurfer requested
    if fs:
        parcels.append('freesurfer_destr')
        parcels.append('freesurfer_desikan')

    # Check for extra multiple parcellations
    if stacked:
        parcels += get_ensemble_options('stacked', add_special=add_special)
    if voted:
        parcels += get_ensemble_options('voted', add_special=add_special)
    if grid:
        parcels += get_ensemble_options('grid', add_special=add_special)

    # Fill in parcel sizes
    parc_sizes = {}
    for parcel in parcels:
        parc_sizes[parcel] = get_parcel_size(parcel, parc_dr)

    # Apply any passed size restrictions
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
        
        # If delete flag remove
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

    # Trunc second half of first table
    t1 = model.summary().tables[0].as_html()
    t1 = t1[:t1.index('<tr>\n  <th>Time:</th>')] + '</table>'
    
    # Replace headers
    t_header = '<table class="simpletable">'
    t_header_new = '<table class="simpletable" style="margin-left: auto; margin-right: auto; width: 75%" align="center">'
    t1 = t1.replace(t_header, t_header_new)
    t2 = model.summary().tables[1].as_html().replace(t_header, t_header_new)
    t2 = t2.replace('width: 75%', 'width: 95%')

    html = '<html><body>' + t1 + '<br>'
    html += t2 + '</body></html>'

    with open('../docs/_includes/' + name + '.html', 'w') as f:
        f.write(html)

def clean_col_names(r_df):

    return r_df.rename({'Mean_Rank': 'Mean Rank', 'r2': 'Mean R2',
                        'roc_auc': 'Mean ROC AUC', 'target': 'Target', 'Model': 'Pipeline',
                        'full_name': 'Parcellation', 'Mean_Score': 'Mean Score'}, axis=1)

def save_results_table(r_df, name):
    
    r_df = clean_col_names(r_df)

    r_df = r_df[['Parcellation', 'Mean Rank', 'Size',
                 'Mean R2', 'Mean ROC AUC']]

    r_df = r_df.sort_values('Mean Rank')

    save_table(r_df, name)
    
def save_table(r_df, name):

    html = '<script src="https://www.kryogenix.org/code/browser/sorttable/sorttable.js"></script>'
    html += r_df.to_html(float_format="%.4f", classes=['sortable'], border=0,
                         index=False, justify='center')

    with open('../docs/_includes/' + name + '.html', 'w') as f:
        f.write(html)

