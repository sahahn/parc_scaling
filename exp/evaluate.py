import time
import numpy as np
import BPt as bp
import os

from models import get_pipe


def _evaluate(args, n_jobs):

    # Save current time to indicate job is started
    np.save(args['save_loc'], np.array([time.time()]))
    os.chmod(args['save_loc'], 0o777)

    # Create the CV group preserve by family id
    cv_strat = bp.CVStrategy(groups='rel_family_id')

    # Get the pipeline to evaluate
    pipeline = get_pipe(model_str=args['model'],
                        parcel=args['parcel'],
                        cv_strat=cv_strat)

    # Load saved dataset, if freesurfer ROI then need dif
    # dataset and scope, otherwise, base option
    if args['parcel'].startswith('freesurfer_'):
        dataset = bp.read_pickle('../data/fs_dataset.pkl')
        scope = args['parcel'].split('_')[-1].upper()
    else:
        dataset = bp.read_pickle('../data/dataset.pkl')
        scope = 'all'

    # Make the problem spec
    ps = bp.ProblemSpec(target=args['target'],
                        n_jobs=n_jobs,
                        scope=scope,
                        random_state=5)

    # CV to evaluate with
    eval_cv = bp.CV(splits=5, n_repeats=1,
                    cv_strategy=cv_strat,
                    only_fold=args['split'])

    # Evaluate
    results = bp.evaluate(pipeline=pipeline,
                          problem_spec=ps,
                          dataset=dataset,
                          cv=eval_cv)
    
    # Get scores from results in special array-like format
    scores = []
    for metric in results.mean_scores:
        summary = [results.mean_scores[metric], results.std_scores[metric], 0]
        scores.append(np.array(summary))

    # Save scores, indicating this job is done
    np.save(args['save_loc'], scores)
    os.chmod(args['save_loc'], 0o777) 

def evaluate(args, n_jobs):
    
    print('Running for: ', args['name'], flush=True)
    
    # Wrap main evaluate loop in custom error handling
    try:
        _evaluate(args, n_jobs)
    
    except Exception as e:
        
        existing = np.load(args['save_loc'])
        elapsed = str(time.time() - existing[0])

        # Append to errors file
        with open('errors.txt', 'a') as f:
            f.write('Error with: ' + args['name'] + ' ')
            f.write('n_jobs: ' + str(n_jobs) + ' Elapsed: ' + elapsed)
            f.write('Error msg: ' + repr(e))
            f.write('\n')

        # If not somehow already done by different job
        if len(existing) == 1:
            
            # Delete job started indicator
            os.remove(args['save_loc'])