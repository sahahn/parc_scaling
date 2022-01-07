from neurotools.transform import SurfLabels, SurfMaps
from BPt import (Model, Pipeline, Scaler,
                 Loader, ParamSearch, FeatSelector,
                 CV, Ensemble, Select, Imputer)
import numpy as np
import os

from config import cache_dr, cache_fit_dr, parcel_dr, extra_parcel_dr, ensemble_max_choice
from config import models as all_model_strs


def get_existing_parcel_names():
    '''Function to get all existing non random and non-ico parcel names.'''
    
    # Get all parcels in folder
    files = os.listdir(parcel_dr)

    # Exclude random + ico
    parcels = [file for file in files if 'random' not in file and 'icosahedron' not in file]
    parcels = [p.replace('.npy', '') for p in parcels]

    return parcels


def get_special_parcel_names(start_str):
    '''Function to help get just a special subset of parcels.'''

    files = os.listdir(parcel_dr)
    parcels = [file.replace('.npy', '') for file in files if file.startswith(start_str)]

    return parcels


def get_random_parcel_names(parcel):
    '''Specific function for getting the correct random base parcel names
    from the passed parcel name.'''

    # Either range or fixed
    parcel_size = parcel.split('_')[2]
    
    # Get number of parcels and the random seed
    n_parcels = int(parcel.split('_')[3])
    parcel_seed = int(parcel.split('_')[4])

    # If parcel size is a range
    if '-' in parcel_size:
        
        # Extract min and max sizes
        sizes = parcel_size.split('-')
        min_size, max_size = int(sizes[0]), int(sizes[1])
        
        # Generate sizes as points between either end,
        # including either end.
        sizes = np.linspace(min_size, max_size, n_parcels).astype('int')
        base_parcels = ['random_' + str(size) + '_' + str(parcel_seed) for size in sizes]

    # Or fixed
    else:
        parcel_size = int(parcel_size)
    
        # If fixed, then we want the starting random parcel to be
        # the maximum size (10) * the parcel seed. So that each repeat between
        # n_parcels == 3 and say 5 is comparable, but so that repeat 2 for 
        # parcels == 3 doesn't overlap with repeat 1's last two parcels in 5 parcels.
        start = int(ensemble_max_choice * parcel_seed)
        end = start + n_parcels
        base_parcels = ['random_' + str(parcel_size) + '_' + str(n) for n in range(start, end)]

    return base_parcels


def get_base_parcel_names(parcel):
    '''Utility for ensemble / extra.'''

    # Check the parcel type, either random or special case
    parcels_type = parcel.split('_')[1]

    # Special cases
    if parcels_type == 'existing':
        return get_existing_parcel_names()
    elif parcels_type == 'schaefer':
        return get_special_parcel_names('schaefer_')
    elif parcels_type == 'mist':
        return get_special_parcel_names('vol-resamp-mist-')
    elif parcels_type == 'icosahedron':
        return get_special_parcel_names('icosahedron-')
    elif parcels_type == 'basc':
        return get_special_parcel_names('vol-resamp-basc-')
    elif parcels_type == 'difumo':
        return get_special_parcel_names('vol-resamp-difumo-')

    # Otherwise is random
    return get_random_parcel_names(parcel)


def get_ensemble_base_models(model_str, parcel, cv_strat=None):
    '''Get explicitly the base models for ensemble / extra style.'''
    
    # Generate special all ensemble if requested
    if model_str == 'all':
        
        base_models = []
        for m_str in all_model_strs:
            base_models += get_ensemble_base_models(m_str, parcel, cv_strat=cv_strat)

        return base_models
    
    # Get the base parcel names
    base_parcels = get_base_parcel_names(parcel)
    
    # Use the parcels to get a full model for each
    # wrapping each pipeline in a Model object
    base_models = [Model(get_pipe(model_str, p,
                                  cv_strat, ensemble=parcel)) for p in base_parcels]
    
    return base_models


def get_grid(model_str, parcel, cv_strat=None):
    '''Get a grid search style pipeline'''
    
    # Get base models
    base_models = get_ensemble_base_models(model_str=model_str,
                                           parcel=parcel, cv_strat=cv_strat)

    # Make it a hyper-parameter choice of which model to use
    choice_of_model = Select(base_models)
    
    # Special param search for this object, using custom CV
    p_cv = CV(splits=3, cv_strategy=cv_strat)
    param_search = ParamSearch('grid', cv=p_cv)

    # Wrap in pipeline, associating choice of model
    # with parameter search
    pipeline = Pipeline(steps=[choice_of_model],
                        param_search=param_search)

    return pipeline


def get_voted(model_str, parcel, cv_strat=None):
    '''Get the voting ensemble style pipeline'''

    # Get base models
    base_models = get_ensemble_base_models(model_str=model_str,
                                           parcel=parcel, cv_strat=cv_strat)
    
    # Create voting ensemble
    voting_ensemble = Ensemble(obj="voting",
                               models=base_models,
                               n_jobs_type='models')
    
    # Wrap in pipeline
    pipeline = Pipeline(steps=[voting_ensemble])

    return pipeline


def get_stacked(model_str, parcel, cv_strat=None):
    '''Get a stacking ensemble style pipeline'''

    # Set the outer combining / stacking model
    stack_param_search = ParamSearch(search_type='RandomSearch',
                                     n_iter=60,
                                     cv=CV(splits=3, n_repeats=1))
    stack_model = Model('ridge', params=1, param_search=stack_param_search)

    # Only do an internal 3-fold CV for generating predictions for stacking
    # this is the same CV split used by the Grid search.
    stack_splits = CV(splits=3, n_repeats=1, cv_strategy=cv_strat)

    # Get base models
    base_models = get_ensemble_base_models(model_str=model_str,
                                           parcel=parcel, cv_strat=cv_strat)
    # Create the stacking ensemble
    stacking_ensemble = Ensemble(obj="stacking",
                                 models=base_models,
                                 cv=stack_splits,
                                 base_model=stack_model,
                                 n_jobs_type='models')

    # Wrap in pipeline
    pipeline = Pipeline(steps=[stacking_ensemble])

    return pipeline


def get_base_model_step(model_str, cv_strat):
    '''Return a base BPt style input Model.'''
    
    # Base parameter search CV
    param_cv = CV(splits=3, n_repeats=1, cv_strategy=cv_strat)
    
    # Base random search
    base_param_search =\
        ParamSearch(search_type='RandomSearch',
                    n_iter=60,
                    cv=param_cv)

    # Define feat selectors with variance threshold and then univariate selection
    feat_selectors =\
        [FeatSelector('variance threshold'),
         FeatSelector('univariate selection', params=2)]

    # Define alternate LGBM param search
    p_cv = CV(splits=.25, n_repeats=1, cv_strategy=cv_strat)
    lgbm_param_search = ParamSearch(search_type='TwoPointsDE',
                                    n_iter=180,
                                    cv=p_cv)
    
    # Elastic-Net option
    if model_str == 'elastic':
        
        model = Model('elastic',
                      params=1,
                      param_search=base_param_search,
                      tol=1e-3,
                      max_iter=1000)
        return [model]

    elif model_str == 'ridge':

        model = Model('ridge',
                      params=1,
                      param_search=base_param_search)
        return [model]

    elif model_str == 'elasticFS':

        # Create nested Elastic-Net
        base_model = Model('elastic',
                           params=1,
                           tol=1e-3,
                           max_iter=1000)

        # As Pipeline
        nested_elastic_pipe = Pipeline(steps=feat_selectors + [base_model],
                                       param_search=base_param_search)
        
        # Return wrapped in Model
        return [Model(nested_elastic_pipe)]
    
    # LGBM option
    elif model_str == 'lgbm':

        model = Model('light gbm',
                      params=1,
                      param_search=lgbm_param_search)

        return [model]

    # LGBM with feature selection option
    elif model_str == 'lgbmFS':

        # Create base LGBM
        base_model = Model('light gbm', params=1)

        # As Pipeline
        nested_lgbm_pipe = Pipeline(steps=feat_selectors + [base_model],
                                    param_search=lgbm_param_search)
           
        # Return wrapped in Model
        return [Model(nested_lgbm_pipe)]

    # SVM option
    elif model_str == 'svm':

        # For svm param search add special search only parameter
        base_param_search.search_only_params = {'svm classifier__probability': False}
        
        # Create nested SVM
        base_model = Model('svm',
                           params=1,
                           cache_size=1500)

        # As Pipeline
        nested_svm_pipe = Pipeline(steps=feat_selectors + [base_model],
                                   param_search=base_param_search)
        
        # Return wrapped in Model
        return [Model(nested_svm_pipe)]
    
    # If none of the above
    raise RuntimeError(f'Invalid model_str: {model_str}')


def get_loader_step(parcel, ensemble):

    # For no parcel / loader
    # Return loader as empty list
    # and parcel_cache_name as None
    if parcel == '':
        return []
    
    # If parcel starts with freesurfer, then
    # instead of a loader, we want to use mean imputation
    # to handle a few missing subjects.
    if parcel.startswith('freesurfer_'):
        return [Imputer('mean')]

    # If not a sub ensemble model
    if ensemble is None:
        parc_loc = os.path.join(parcel_dr, parcel + '.npy')
        cache_loc = os.path.join(cache_dr, parcel)

    # Otherwise, the name of the base ensemble model,
    # e.g., stacked_random_100_3_0 is passed as ensemble
    else:
        parc_loc = os.path.join(extra_parcel_dr, parcel + '.npy')
        cache_loc = os.path.join(cache_dr, parcel + '_e')

        # Special case - for ensembles of existing use base parcel dr
        if not os.path.exists(parc_loc):
            parc_loc = os.path.join(parcel_dr, parcel + '.npy')
            cache_loc = os.path.join(cache_dr, parcel)
    
    # Depending on type of parcellation use SurfMaps or Labels
    if len(np.load(parc_loc).shape) == 2:
        rois = SurfMaps(maps=parc_loc)
    else:
        rois = SurfLabels(labels=parc_loc)
    
    # Make loader
    loader = Loader(rois, cache_loc=cache_loc)
    
    # Return as list
    return [loader]


def get_pipe(model_str, parcel, cv_strat=None, ensemble=None):

    print('Get pipeline with:', model_str,
          parcel, cv_strat, flush=True)

    # First check to see if special ensemble / extra option
    # based on passed parcel name
    if parcel.startswith('stacked_'):
        return get_stacked(model_str, parcel, cv_strat=cv_strat)
    
    elif parcel.startswith('voted_'):
        return get_voted(model_str, parcel, cv_strat=cv_strat)
    
    elif parcel.startswith('grid_'):
        return get_grid(model_str, parcel, cv_strat=cv_strat)

    # Get loader as list
    loader = get_loader_step(parcel, ensemble=ensemble)

    # Use robust scaling
    scaler = [Scaler('robust')]
    
    # Get base model as list
    model = get_base_model_step(model_str, cv_strat)
    
    # Set cache fit loc for only ensembles,
    # as the different pipelines for different parcels are re-used
    cache_fit_loc = None
    if ensemble is not None:
        cache_fit_loc = os.path.join(cache_fit_dr, parcel + '_e')
    print('cache_fit_loc:', cache_fit_loc, flush=True)
    
    # Base pipeline steps are loading, then scaling, then model
    steps = loader + scaler + model
    pipeline = Pipeline(steps=steps,
                        cache_loc=cache_fit_dr)
                        
    return pipeline
