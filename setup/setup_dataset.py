import pandas as pd
import BPt as bp
import os
import numpy as np

def load_base(filter_outliers=True):
    
    # Load as dataset, and set verbose on
    data = bp.Dataset(pd.read_csv('../data/targets.csv', index_col='src_subject_id'))
    data.verbose = 1
    
    # Set everything as target first
    data.set_target('all', inplace=True)
    
    # Ordinalize rel family id and set as non input
    data.ordinalize('rel_family_id', inplace=True)
    data.set_role('rel_family_id', 'non input', inplace=True)
    
    # Auto detect any categorical
    data = data.auto_detect_categorical()

    # Binarize all categorical, from just target
    data = data.to_binary(scope='target category', drop=False)
    
    # Filter any extreme outliers from just target
    if filter_outliers:
        data = data.filter_outliers_by_std(n_std=10, scope='target float', drop=False)
    
    return data

def get_files():
    
    files = {}
    dr = os.path.abspath('../data/abcd_structural/')
    modals = os.listdir(dr)

    for modal in modals:
        
        files[modal] = []
        
        m_dr = os.path.join(dr, modal)
        for file in os.listdir(m_dr):
            file_loc = os.path.join(m_dr, file)
            files[modal].append(file_loc)

    return files

def file_to_subject_func(file):
    subject = 'NDAR_' + file.split('/')[-1].replace('.npy', '')
    return subject

def load_data(data, filter_outliers=True):

    # Load all of the data files
    data = data.add_data_files(files=get_files(),
                               file_to_subject=file_to_subject_func)
    print('Loaded Data Files:', data.shape)
    
    if filter_outliers:
    
        # Drop by just std
        data.filter_outliers_by_std(n_std=10,
                                    scope=['myelin', 'thick', 'sulc'],
                                    reduce_func=np.std,
                                    n_jobs=16,
                                    inplace=True)
        
        # Drop w/ 3 funcs sequentially
        for func in [np.min, np.max, np.std]:
            data.filter_outliers_by_std(n_std=10,
                                        scope='curv',
                                        n_jobs=16,
                                        reduce_func=func,
                                        inplace=True)
        
        # Drop NaN subjects from data / non input here
        data = data.drop_nan_subjects(scope=['data', 'non input'])
        
    return data

def get_dataset(load_compat=True, consolidate=True):
    '''Because a few order or operations things changed between versions,
    we can either do something very close to the original processing or
    load the explicit valid subjects.'''
    
    data = load_base(filter_outliers=not load_compat)
    data = load_data(data, filter_outliers=not load_compat)
    
    if load_compat:
        data.apply_inclusions('../data/valid_subjects.txt', inplace=True)

    if consolidate:
        data.consolidate_data_files(save_dr='../data/consolidated',
                                    cast_to='float32',
                                    replace_with='consolidated',
                                    clear_existing=False)
    
    return data

def main():
    
    # Load dataset, with compat and consolidate
    data = get_dataset(load_compat=True, consolidate=True)
    print('Final Dataset Shape:', data.shape)
    
    # Save to data
    data.to_pickle('../data/dataset.pkl')
    
    # Save some info as a docx table
    data.summary('target', measures=['count', 'mean +- std', 'nan count'],
                 decimals=2, save_file='targets.docx')

if __name__ == "__main__":
    main()