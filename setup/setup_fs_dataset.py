from setup_dataset import load_base
import pandas as pd

def main():
    
    # Load dataset with targets and family_id
    data = load_base(filter_outliers=True)
    
    # Get base_subjects from main dataset, as we want these to match
    base_data = pd.read_pickle('../data/dataset.pkl')
    base_subjects = base_data.index
    data = data.loc[base_subjects]
    
    def add_fs_data(loc, suffix):

        # Load ROIs
        fs_data = pd.read_csv(loc)
        fs_data['src_subject_id'] = [s.replace('NDAR', 'NDAR_') for s in fs_data['src_subject_id']]
        
        # Reduce to just keep features
        keep = ['_thickavg', '_surfarea', '_meancurv']
        to_keep = [col for col in list(fs_data) if any([k in col for k in keep])]
        fs_data = fs_data[to_keep]
        
        # Add to data with suffix
        for col in fs_data:
            data[col + suffix] = fs_data[col]
    
    # Add both
    add_fs_data('../data/aparc.a2009s_rois.csv', '-DESTR')
    add_fs_data('../data/aparc_rois.csv', '-DESIKAN')
    
    # Save with pickle to data
    data.to_pickle('../data/fs_dataset.pkl')

if __name__ == '__main__':
    main()
