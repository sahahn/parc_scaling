import sys

from helpers import get_choice, check_if_done
from evaluate import evaluate

def unpack_args():

     # Get n_jobs
    passed_args = list(sys.argv)
    n_jobs = int(passed_args[1])

    try:
        c = int(passed_args[2])

    # Default to choice 0 if not passed
    except IndexError:
        c = 0
    
    # If passed as str
    except ValueError:
        return [passed_args[2]], n_jobs

    # Choice of only by passed choice
    if c == 0:
        only = ['elastic', 'svm']
    elif c == 1:
        only = ['lgbm']
    elif c == 2:
        only = ['elastic']
    elif c == 3:
        only = ['svm']
    elif c == 4:
        only = ['all', 'elastic', 'svm', 'lgbm']
    else:
        only = ['elastic', 'svm', 'lgbm']

    return only, n_jobs

def main():

    # Unpack arguments
    only, n_jobs = unpack_args()

    # Select a choice, getting it's arguments
    args = get_choice(only=only)
    print('Selected Choice:', args, flush=True)
    
    # If no choices left
    if args is None:
        sys.exit()

    # Check to make sure another overlapping job
    # didn't already start
    if check_if_done(args['save_loc']):
        print('Job is already started, cancelling.', flush=True)
        sys.exit()

    # Run evaluate, pass args and n_jobs
    evaluate(args, n_jobs)

if __name__ == '__main__':
    main()