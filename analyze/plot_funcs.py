import numpy as np
import matplotlib.pyplot as plt
import os
import seaborn as sns
import pandas as pd
from IPython.display import display
from funcs import get_parc_sizes
from scipy.stats import kstest
from scipy.stats import linregress, theilslopes


target_map = {
           'anthro_height_calc': 'Standing Height (inches)',
           'anthro_weight_calc': 'Measured Weight (lbs)',
           'anthro_waist_cm': 'Waist Circumference (inches)',
           'devhx_20_motor_dev_p': 'Motor Development',
           'cbcl_scr_syn_rulebreak_r': 'CBCL RuleBreak Syndrome Scale',
           'demo_prnt_age_p': 'Parent Age (yrs)',
           'devhx_2_birth_wt_lbs_p': 'Birth Weight (lbs)',
           'interview_age': 'Age (months)',
           'lmt_scr_perc_correct': 'Little Man Test Score',
           'macvs_ss_r_p': 'MACVS Religion Subscale',
           'neighb_phenx_ss_mean_p': 'Neighborhood Safety',
           'neurocog_pc1.bl': 'NeuroCog PCA1 (general ability)',
           'neurocog_pc2.bl': 'NeuroCog PCA2 (executive function)',
           'neurocog_pc3.bl': 'NeuroCog PCA3 (learning / memory)',
           'nihtbx_cardsort_uncorrected': 'NIH Card Sort Test',
           'nihtbx_list_uncorrected': 'NIH List Sorting Working Memory Test',
           'nihtbx_pattern_uncorrected': 'NIH Comparison Processing Speed Test',
           'nihtbx_picvocab_uncorrected': 'NIH Picture Vocabulary Test',
           'nihtbx_reading_uncorrected': 'NIH Oral Reading Recognition Test',
           'pea_wiscv_trs': 'WISC Matrix Reasoning Score',
           'sports_activity_activities_p_performance': 'Summed Performance Sports Activity',
           'sports_activity_activities_p_team_sport': 'Summed Team Sports Activity',
           'accult_phenx_q2_p': 'Speaks Non-English Language',
           'asr_scr_thought_r_binary': 'Thought Problems ASR Syndrome Scale',
           'cbcl_scr_syn_aggressive_r_binary': 'CBCL Aggressive Syndrome Scale',
           'devhx_12a_born_premature_p': 'Born Premature',
           'devhx_15_days_incubator_p_binary': 'Incubator Days',
           'devhx_18_mnths_breast_fed_p_binary': 'Months Breast Feds',
           'devhx_5_twin_p': 'Has Twin',
           'devhx_6_pregnancy_planned_p': 'Planned Pregnancy',
           'devhx_distress_at_birth_binary': 'Distress At Birth',
           'devhx_mother_probs_binary': 'Mother Pregnancy Problems',
           'devhx_ss_alcohol_avg_p_binary': 'Any Alcohol During Pregnancy',
           'devhx_ss_marijuana_amt_p_binary': 'Any Marijuana During Pregnancy',
           'screentime_week_p_binary': 'Screen Time Week',
           'screentime_weekend_p_binary': 'Screen Time Weekend',
           'ksads_adhd_composite_binary': 'KSADS ADHD Composite',
           'ksads_bipolar_composite_binary': 'KSADS Bipolar Composite',
           'ksads_OCD_composite_binary': 'KSADS OCD Composite',
           'sex_at_birth': 'Sex at Birth',
           'sleep_ss_total_p_binary': 'Sleep Disturbance Scale',
           'ksads_back_c_det_susp_p': 'Detentions / Suspensions',
           'ksads_back_c_mh_sa_p': 'Mental Health Services',
           'married.bl': 'Parents Married',
           'prodrom_psych_ss_severity_score_binary': 'Prodromal Psychosis Score'}

rev_target_map = {target_map[k]: k for k in target_map}


def plot_avg_ranks(results, only_targets=None, across=False,
                   raw=False, model='average',
                   rank_type='Mean_Rank', log=False,
                   ax=None, sm=1, sep_dif_sizes=False, **kwargs):

    df, parc_sizes = get_results_df(results, only_targets=only_targets, **kwargs)
    
    if across:
        plot_rank_comparison(parc_sizes, df, log=log, ax=ax,
                             sm=sm)
    else:

        if raw:
            plot_raw_scores(parc_sizes, df, model=model, log=log)
        else:
            plot_ranks(parc_sizes, df, model=model,
                       rank_type=rank_type, log=log, ax=ax, sm=sm,
                       sep_dif_sizes=sep_dif_sizes)

def get_results_df(results, only_targets=None, **kwargs):

    if 'size_max' not in kwargs:
        kwargs['size_max'] = 20000
    
    parc_sizes = get_parc_sizes('../parcels', **kwargs)
    df = conv_to_df(results, only=parc_sizes, only_targets=only_targets)

    return df, parc_sizes

def remove_duplicate_labels(ax):

    handles, labels = ax.get_legend_handles_labels()
    by_label = dict(zip(labels, handles))
    ax.legend(by_label.values(), by_label.keys(), loc=1, fontsize=12)

def check_powerlaw(xs, ys, trunc=None, e_trunc=None, add_to_log=False, color=None):

    if trunc is not None:
        xs = xs[trunc:]
        ys = ys[trunc:]
    if e_trunc is not None:
        xs = xs[:-e_trunc]
        ys = ys[:-e_trunc]

    r = linregress(np.log10(xs), np.log10(ys))

    if add_to_log:
        plt.plot(xs, 10**(r.intercept) * (xs **(r.slope)), color=color)
    else:
        plt.plot(np.log10(xs), r.slope*np.log10(xs) + r.intercept)
        plt.scatter(np.log10(xs), np.log10(ys))
    
    print('linregress slope:', r.slope, 'linregress rvalue:', r.rvalue)
    ts = theilslopes(np.log10(ys), np.log10(xs))
    print('Theil-Sen slope:', ts[0], '95% CI:', ts[2], ts[3])

def get_divergence(ij, in_xs, in_ys, plot=False):
    
    i, j = ij
    
    if i < 0 or j < 0:
        return 10000
    
    j = -j
    if j == 0:
        j = None
    
    xs = in_xs.copy()[i:j]
    ys = in_ys.copy()[i:j]
    
    # Estimate fit
    r = linregress(np.log10(xs), np.log10(ys))
    
    # Get points from what should be fit
    p_ys = 10**(r.intercept) * (xs **(r.slope))
    
    k = kstest(ys, p_ys).statistic
    
    if plot:
        plt.scatter(xs, p_ys)
        plt.scatter(xs, ys)
        print(k)
    
    # Return kstest
    return k

def get_rt(df):

    cols = list(df)
    cols = [col for col in cols if col.endswith('_Rank')]
    return cols[0]

def get_min_max_bounds(r_df, plot=False):
    
    # To array
    xs = np.array(r_df['Size'])
    ys = np.array(r_df[get_rt(r_df)])
 
    up_to = len(xs) // 4

    # First estimate lower bound
    options = [(i, 0) for i in range(up_to)]
    divergences = [get_divergence(o, xs, ys) for o in options]
    i = options[np.argmin(divergences)][0]

    # Estimate upper based on lower
    options = [(i, j) for j in range(up_to)]
    divergences = [get_divergence(o, xs, ys) for o in options]
    j = options[np.argmin(divergences)][1]
    
    if plot:
        get_divergence((i, j), xs, ys, plot=True)
        
    return i, j

def get_results(results_dr):

    results = {}
    incomplete_cnt = 0
    result_files = os.listdir(results_dr)

    for file in result_files:
        
        result = np.load(os.path.join(results_dr, file))
        name = file.replace('.npy', '')
        
        if len(file.split('---')) == 3:

            if len(result) > 1:
                results[name] = result
            else:
                incomplete_cnt += 1
                
        else:
            
            # Get correct name
            name = '---'.join(name.split('---')[:-1])
            
            if len(result) > 1:
                
                try:
                    results[name].append(result)
                except KeyError:
                    results[name] = [result]
                    
                # Once all 5 loaded, format correctly
                if len(results[name]) == 5:
                    
                    to_fill = results[name][0].copy()
                    to_fill[:,0] = np.mean(results[name], axis=0)[:,0]
                    to_fill[:,1] = np.std(results[name], axis=0)[:,0]
                    results[name] = to_fill

            else:
                incomplete_cnt += .2
            
    print('Found:', len(results), 'Incomplete:', incomplete_cnt)
            
    return results

def conv_to_df(results, only=None, only_targets=None):
    
    # Check for if passed as formatted names
    if only_targets is not None:
        if only_targets[0] in list(rev_target_map):
            only_targets = [rev_target_map[t] for t in only_targets]
    
    parcels, models = [], []
    targets, scores = [], []
    stds, is_binary = [], []

    for result in results:

        split = result.split('---')
        
        # Restrict to only some parcellations
        if only is not None:
            if split[0] not in only:
                continue
        
        # Restrict to only some targets
        if only_targets is not None:
            if split[2] not in only_targets:
                continue
                
        # If chunked score, skip
        if isinstance(results[result], list):
            continue

        # Add to lists
        parcels.append(split[0])
        models.append(split[1])
        targets.append(split[2])
        score = results[result]
        
        # If regression
        if len(score) == 2:
            scores.append(score[0][0]) 
            stds.append(score[0][1])
            is_binary.append(False)

        # If binary
        else:
            scores.append(score[1][0])
            stds.append(score[1][1])
            is_binary.append(True)

    df = pd.DataFrame()
    df['parcel'] = parcels
    df['model'] = models
    df['is_binary'] = is_binary
    df['target'] = targets
    df['score'] = scores
    df['std'] = stds
    
    df = df.set_index(['model', 'parcel']).sort_index()
    
    return df

def plot_score_by_n(parc_sizes, scores, title, ylabel, xlim=1050,
                    log=False, ax=None, sm=1, sep_dif_sizes=False):
    
    # To handle either adding to existing plot or
    # generate new plot.
    if ax is None:
        _, ax = plt.subplots(figsize=(12, 8))
    
    # Use viridis color map
    cmap = plt.get_cmap('viridis')

    scores.index = ['a_' + p if 'freesurfer' in p else p for p in scores.index]
   
    # Sort
    scores = scores.sort_index(ascending=False)
    
    for parcel in scores.index:
        
        s = 100
        score = scores.loc[parcel]
                    
        if parcel.startswith('stacked_random_'):
            color = 'mediumblue'
            alpha = 1
            label = 'Stacked'
            marker = "+"
            s = 125

        elif parcel.startswith('voted_random_'):
            color = 'green'
            alpha = 1
            label = 'Voted'
            marker = "+"
            s = 125

        elif parcel.startswith('grid_random_'):
            color = 'purple'
            alpha = 1
            label = 'Grid'
            marker = "+"
            s = 125

        elif 'icosahedron' in parcel:
            color = cmap(0)
            alpha = 1
            label = 'Icosahedron'
            marker = 'p'

        elif 'random' in parcel:
            color = 'black'
            alpha = .5
            label = 'Random'
            marker = "+"
            
        elif 'freesurfer' in parcel:
            parcel = parcel.replace('a_', '')
            color = 'orange'
            alpha = 1
            label = 'Freesurfer Extracted'
            marker = "*"
            s = 150
        
        # Base
        else:
            alpha = .75
            color = cmap(.7)
            label = 'Existing'
            marker = "o"

        if sep_dif_sizes and '-' in parcel:
            marker = 'x'
            label += ' (across sizes)'

        n_parcels = parc_sizes[parcel]
        ax.scatter(n_parcels, score,
                   color=color, alpha=alpha,
                   label=label, marker=marker, s=s*sm)

    # Clean y label and add
    ylabel = ylabel.replace('_', '')
    ax.set_ylabel(ylabel, fontsize=16)

    # Set x label
    ax.set_xlabel('Size / Num. Parcels', fontsize=16)

    # Finishing touches
    _finish_plot(ax, title, xlim, log)
    
def plot_scores(parc_sizes, means, ylabel, model='average', **plot_args):

    if model == 'svm':
        plot_score_by_n(parc_sizes, means.loc[model], 'SVM', ylabel, xlim=None, **plot_args)
    elif model == 'lgbm':
        plot_score_by_n(parc_sizes, means.loc[model], 'LGBM', ylabel, xlim=None, **plot_args)
    elif model == 'elastic':
        plot_score_by_n(parc_sizes, means.loc[model], 'Elastic-Net', ylabel, xlim=None, **plot_args)
    elif model =='all':
        plot_score_by_n(parc_sizes, means.loc[model], 'All-Ensemble', ylabel, xlim=None, **plot_args)
    else:
        # Exclude all here!
        parc_means = means.loc[['svm', 'elastic', 'lgbm']].groupby('parcel').mean()
        plot_score_by_n(parc_sizes, parc_means,
                        'Mean Across Pipelines', ylabel,
                        xlim=None, **plot_args)

def get_rank_func(rank_type):

    if rank_type in ['Mean_Rank', 'mean']:
        return mean_rank
    elif rank_type in ['Median_Rank', 'median']:
        return median_rank
    elif rank_type in ['Max_Rank', 'max']:
        return max_rank
    elif rank_type in ['Min_Rank', 'min']:
        return min_rank

    raise RuntimeError(f'Invalid rank_type: {rank_type}')

def get_score_func(rank_type):

    if rank_type in ['Mean_Rank', 'mean']:
        return mean_score
    elif rank_type in ['Median_Rank', 'median']:
        return median_score

    # Swap max and min
    elif rank_type in ['Max_Rank', 'max']:
        return min_score
    elif rank_type in ['Min_Rank', 'min']:
        return max_score

    raise RuntimeError(f'Invalid rank_type: {rank_type}')

def _get_ranks_df(df):

    # Get as parcel df
    parcel_df = df.reset_index().set_index('parcel')

    # Then convert to rank order
    ranks = parcel_df.groupby(['model', 'target']).apply(get_rank_order)

    # Set as correct DataFrame
    ranks = ranks.to_frame().reset_index()

    return ranks

def get_summary_ranks(r_df, rank_type='Mean_Rank', models='default'):

    if models == 'default':
        models = ['svm', 'elastic', 'lgbm']

    # Get base ranks
    ranks = _get_ranks_df(r_df)

    # Get rank func from type
    rank_func = get_rank_func(rank_type)

    # Apply rank func
    avgs = ranks.groupby(['model', 'parcel']).apply(rank_func)
    parcel_avgs = avgs.loc[models].groupby('parcel').mean()
    
    return pd.DataFrame(parcel_avgs, columns=[rank_type])

def get_model_avg_ranks(df):
    
    # Get base ranks
    ranks = _get_ranks_df(df)

    means = ranks.groupby(['target', 'parcel']).apply(mean_rank)
    scores = df.reset_index().groupby(['target', 'parcel']).apply(mean_score)

    return_df = means.to_frame().rename(columns={0: 'Mean_Rank'})
    return_df['Mean_Score'] = scores

    return return_df.reset_index().set_index('parcel')

def get_cut_off_df(r_df):
    
    r_df = r_df.sort_values('Size')
    i, j = get_min_max_bounds(r_df)

    j = -j
    if j == 0:
        j = None

    print(i, j)

    return r_df.iloc[i:j]

def get_intra_pipeline_df(results, log=False,
                          threshold=False,
                          models='default',
                          rank_type='Mean_Rank',
                          **kwargs):

    if models == 'default':
        models = ['lgbm', 'elastic', 'svm']
    
    # Get each one w/ ranks seperately
    r_dfs = []

    for model in models:
        r_df = get_ranks_sizes(results, log=log,
                               models=[model],
                               threshold=threshold,
                               rank_type=rank_type,
                               **kwargs)
        r_df['Model'] = model
        r_dfs.append(r_df)

    intra_pipe_df = pd.concat(r_dfs)

    # Clean model names
    intra_pipe_df = clean_model_names(intra_pipe_df)
    
    # Return w/ model name changed
    return intra_pipe_df.rename({'Model': 'Pipeline'}, axis=1)

def get_inter_pipe_df(results, models='default',
                      log=False, rank_type='Mean_Rank',
                       **kwargs):

    if models == 'default':
        models = ['lgbm', 'elastic', 'svm']

    # Get inter pipe df
    inter_pipe_df = clean_model_names(
        get_across_ranks(results, models=models,
                         log=log, rank_type=rank_type,
                         **kwargs))
    
    # Return
    return inter_pipe_df.rename({'Model': 'Pipeline'}, axis=1)

def _add_raw(df, pm_df, rank_type, models):

    if models == 'default':
        models = ['svm', 'elastic', 'lgbm']

    # Get correct score func
    score_func = get_score_func(rank_type)

    # Calculate by score func summary
    split_avgs = df.groupby(['is_binary', 'model', 'parcel']).apply(score_func)

    # Get mean across models separate for regression / binary per parcellation
    regression_means = split_avgs.loc[False, models].groupby('parcel').apply(np.mean)
    binary_means = split_avgs.loc[True, models].groupby('parcel').apply(np.mean)

    # Add to df
    pm_df['r2'] = regression_means
    pm_df['roc_auc'] = binary_means

    return pm_df

def get_ranks_sizes(results, by_group=True,
                    avg_targets=True,
                    log=False, log_raw=False,
                    threshold=False,
                    only_targets=None, add_raw=False,
                    models='default',
                    keep_full_name=False,
                    add_ranks_labels=False,
                    binary_only=False,
                    regression_only=False,
                    rank_type='Mean_Rank',
                    **kwargs):

    # Base get results df
    df, parc_sizes = get_results_df(results, only_targets=only_targets, **kwargs)

    # Set to subset of models here
    if models == 'default':
        models = ['svm', 'elastic', 'lgbm']
    df = df.loc[models]

    # If binary or regression only
    if binary_only:
        df = df[df['is_binary']]
    if regression_only:
        df = df[~df['is_binary']]
    
    # Base case is average over targets
    if avg_targets:
        pm_df = get_summary_ranks(df, rank_type=rank_type, models=models)

    # Otherwise, only average over models to get ranks
    else:
        pm_df = get_model_avg_ranks(df)
        pm_df = target_to_name(pm_df)

    pm_df['Size'] = [parc_sizes[p] for p in pm_df.index]

    # Use powerlaw threshold if requested
    if threshold:
        pm_df = get_cut_off_df(pm_df)
        print('Smallest size:', pm_df.sort_values('Size').iloc[0].Size)
        print('Largest size:', pm_df.sort_values('Size').iloc[-1].Size)

    # If request add raw scores - as following same type as rank, w/ mean / median / min / max
    if add_raw:
        pm_df = _add_raw(df, pm_df, rank_type, models)

    # If request to add rank labels
    if add_ranks_labels:
        base = f'{rank_type}: ' + pm_df[rank_type].round(3).astype(str)
        extra = f'<br>log10({rank_type}): ' + np.log10(pm_df[rank_type]).round(3).astype(str)
        pm_df['rank_label'] = base + extra

        base = 'Size: ' + pm_df['Size'].astype(str)
        extra = '<br>log10(Size): ' + np.log10(pm_df['Size']).round(3).astype(str)
        pm_df['size_label'] = base + extra

    # If log results
    if log:
        pm_df[rank_type] = np.log10(pm_df[rank_type])
        pm_df['Size'] = np.log10(pm_df['Size'])

    if log_raw:
        if 'r2' in pm_df:
            pm_df['r2'] = np.log10(pm_df['r2'])
        if 'roc_auc' in pm_df:
            pm_df['roc_auc'] = np.log10(pm_df['roc_auc'])

    if not by_group:
        
        # Pretty hacky... but
        if keep_full_name:
            temp = pm_df.reset_index()
            temp['full_name'] = temp['parcel'].apply(clean_name)
            temp = temp.set_index('parcel')
            pm_df['full_name'] = temp['full_name']

        return pm_df

    # Set another column to group
    r_df = pm_df.reset_index()

    if keep_full_name:
        r_df['full_name'] = r_df['parcel'].copy().apply(clean_name)

    # Add labels by parcel
    groups = []
    for parcel in r_df['parcel']:

        if parcel.startswith('stacked_'):
            if parcel.startswith('stacked_random_'):
                label = 'Stacked'
            else:
                label = 'Stacked Special'

        elif parcel.startswith('voted_'):
            if parcel.startswith('voted_random_'):
                label = 'Voted'
            else:
                label = 'Voted Special'

        elif parcel.startswith('grid_'):
            if parcel.startswith('grid_random_'):
                label = 'Grid'
            else:
                label = 'Grid Special'

        elif 'icosahedron' in parcel:
            label = 'Icosahedron'

        elif 'random' in parcel:
            label = 'Random'

        elif 'freesurfer' in parcel:
            label = 'Freesurfer Extracted'

        else:
            label = 'Existing'
        
        groups.append(label)

    r_df['parcel'] = groups
    r_df = r_df.rename({'parcel': 'Parcellation_Type'}, axis=1)

    return r_df

def get_across_ranks(results, only_targets=None,
                     log=False,
                     models='default',
                     keep_full_name=True,
                     rank_type='Mean_Rank',
                     **kwargs):

    # Get base results df
    df, parc_sizes = get_results_df(results, only_targets=only_targets,
                                    **kwargs)

    # Set to subset of models here
    if models == 'default':
        models = ['svm', 'elastic', 'lgbm']
    df = df.loc[models]

    # Get base ranks sep by just target
    parcel_df = df.reset_index().set_index('parcel')
    ranks = parcel_df.groupby(['target']).apply(get_rank_model_order)
    
    # Get requested rank func and use to gen scores
    rank_func = get_rank_func(rank_type)
    avg_ranks = ranks.groupby(['model', 'parcel']).apply(rank_func)
    scores = avg_ranks.reset_index()
    
    # Update names of columns
    scores = scores.rename(columns={0: rank_type,
                                   'model': 'Model',
                                   'parcel': 'Parcellation'})

    # Add full name if requested
    if keep_full_name:
        scores['full_name'] = scores['Parcellation'].copy().apply(clean_name)
    
    # Add size
    scores['Size'] = [parc_sizes[p] for p in scores['Parcellation']]

    # Log size and rank if requested
    if log:
        scores['Size'] = np.log10(scores['Size'])
        scores[rank_type] = np.log10(scores[rank_type])

    return scores

def mean_score(df):
    return df['score'].mean()

def median_score(df):
    return df['score'].median()

def max_score(df):
    return df['score'].max()

def min_score(df):
    return df['score'].min()

def mean_rank(df):
    return df['rank'].mean()

def median_rank(df):
    return df['rank'].median()

def max_rank(df):
    return df['rank'].max()

def min_rank(df):
    return df['rank'].min()

def get_rank_order(df):
     
    # Sort so that best is at top
    df = df.sort_values('score', ascending=False)

    # Set ranks s.t., best has rank 1
    df['rank'] = np.arange(1, len(df)+1)

    return df['rank']

def get_rank_model_order(df):
    
    # Sort so that best is at top
    df = df.sort_values('score', ascending=False)
    
    # Set ranks s.t., best has rank 1
    df['rank'] = np.arange(1, len(df)+1)

    return df[['rank', 'model']]

def plot_ranks(parc_sizes, df, rank_type='mean',
               model='average', **plot_args):
    
    # Get base ranks
    ranks = _get_ranks_df(df)

    # Get rank func
    rank_func = get_rank_func(rank_type)

    # Get summary ranks
    summary_ranks = ranks.groupby(['model', 'parcel']).apply(rank_func)

    # Then plot
    plot_scores(parc_sizes, summary_ranks,
                ylabel=rank_type, model=model, **plot_args)

def _finish_plot(ax, title, xlim, log):

    ax.legend()
    remove_duplicate_labels(ax)
    
    if xlim is not None:
        ax.set_xlim(-10, xlim)

    ax.xaxis.set_tick_params(labelsize=14)
    ax.yaxis.set_tick_params(labelsize=14)

    if log:
        ax.set_xscale('log')
        ax.set_yscale('log')
    
    ax.set_title(title, fontsize=20)

def plot_rank_comparison(parc_sizes, df,
                         title='Mean Rank Across Model Pipeline',
                         xlim=None, log=False, ax=None, sm=1):

    parcel_df = df.reset_index().set_index('parcel')
    ranks = parcel_df.groupby(['target']).apply(get_rank_model_order)

    mean_ranks = ranks.groupby(['model', 'parcel']).apply(mean_rank)
    scores = mean_ranks.reset_index()

    if ax is None:
        _, ax = plt.subplots(figsize=(12, 8))

    cmap = plt.get_cmap('viridis')

    for ind in scores.index:
        
        s = 100
        marker = "o"
        alpha = .5
        
        score = scores.loc[ind, 0]
        model = scores.loc[ind, 'model']
        parcel = scores.loc[ind, 'parcel']
        
        if model == 'svm':
            color = cmap(.2)
            label = 'SVM'
        elif model == 'elastic':
            color = cmap(.5)
            label = 'Elastic-Net'
        elif model == 'lgbm':
            color = cmap(.8)
            label = 'LGBM'
        elif model == 'all':
            color = 'black'
            label = 'All'
        else:
            print('SKIPPING Model = ', model)
            
        n_parcels = parc_sizes[parcel]
        ax.scatter(n_parcels, score,
                   color=color, alpha=alpha,
                   label=label, marker=marker, s=s*sm)

    ax.set_ylabel('Mean Rank', fontsize=16)
    ax.set_xlabel('Num. Parcels', fontsize=16)

    _finish_plot(ax, title, xlim, log)

def plot_raw_scores(parc_sizes, df, avg_only=False, log=False):
    
    split_means = df.groupby(['is_binary', 'model', 'parcel']).apply(mean_score)

    regression_means = split_means.loc[False]
    binary_means = split_means.loc[True]

    plot_scores(parc_sizes, regression_means,
                ylabel='Avg R2',
                avg_only=avg_only, log=log)
    plot_scores(parc_sizes, binary_means,
                ylabel='Avg ROC AUC',
                avg_only=avg_only, log=log)
    
def check_best(df, top_vals=[1, 3, 5, 10]):
    
    models_in_top = {t : [] for t in top_vals}

    for target in df.target.unique():

        top_x = df[df['target'] == target].sort_values('score', ascending=False).head(top_vals[-1])

        # Compute stats
        for i in top_vals:
            models = [top_x.index[j][0] for j in range(i)]
            models_in_top[i] += models

        display(top_x)

    for i in top_vals:

        sns.countplot(models_in_top[i])
        plt.title('Models in Top ' + str(i))
        plt.show()
        
def check_best_by_model(df, models='default'):

    if models == 'default':
        models = ['elastic', 'svm', 'lgbm']
    
    # Top specific to each model for each target
    for model in models:
        print('Model:', model)

        for target in df.target.unique():
            display(df[df['target'] == target].loc[model].sort_values('score', ascending=False).head(5))

def get_single_vs_multiple_df(results, **kwargs):

    r_df = get_ranks_sizes(results, by_group=False, **kwargs)
    r_df = r_df.reset_index().rename(columns={'parcel': 'Parcellation_Type'})

    def set_parc(row):

        # Set if across sizes
        row['across_sizes'] = 0
        if '-' in row['Parcellation_Type']:
            row['across_sizes'] = 1

        row['is_ensemble'] = 0

        # Set as ensemble type or Single
        if 'grid_' in row['Parcellation_Type']:
            row['Parcellation_Type'] = 'Grid'
        elif 'stacked_' in row['Parcellation_Type']:
            row['Parcellation_Type'] = 'Stacked'
            row['is_ensemble'] = 1
        elif 'voted_' in row['Parcellation_Type']:
            row['Parcellation_Type'] = 'Voted'
            row['is_ensemble'] = 1
        else:
            row['Parcellation_Type'] = 'Single'

        return row

    # Prep data frame for plotting
    r_df = r_df.apply(set_parc, axis=1)
    r_df = r_df.set_index('Parcellation_Type')
    
    return r_df

def add_extra_ticks(ax, ref, r2_extra_ticks, roc_extra_ticks):

    # Get name of rank col
    rank_col = get_rt(ref)
    
    ticks = ax.get_yticks()
    ticks = sorted(list(ticks) + r2_extra_ticks + roc_extra_ticks)

    new_labels = []
    for tick in ticks:

        label = str(int(tick)).rjust(3)
        closest = ref.iloc[(ref[rank_col] - tick).abs().argsort()[:1]]

        if int(tick) in r2_extra_ticks:
            r2 =  "%.3f" % closest['r2']
            r2 = r2.replace('0.', '.')
            label = f'[r2~={r2}]  '

        if int(tick) in roc_extra_ticks:
            roc =  "%.3f" % closest['roc_auc'].replace('0.', '.')
            roc = roc.replace('0.', '.')
            label = f'[auc~={roc}]  '

        new_labels.append(label)

    ax.set_yticks(ticks)
    ax.set_yticklabels(new_labels)
    ax.yaxis.set_label_coords(-.075, .5)

def get_highest_performing_df(results, **kwargs):
    
    # Get just svm non random existing
    non_random_single, parc_sizes = get_results_df(results, base=True, ico=True, fs=True, **kwargs)
    non_random_single.rename(index={'svm': 'existing'}, inplace=True)
    
    # Get just stacked and voted
    ensemble, parc_sizes_ensemble = get_results_df(results, stacked=True, voted=True, **kwargs)
    
    # Make combined df
    df = pd.concat([non_random_single, ensemble])
    parc_sizes.update(parc_sizes_ensemble)
    
    # Restrict to only all and svm
    df = df.drop(['elastic', 'lgbm',
                  'elasticFS', 'lgbmFS'], level=0)

    # Get as explicit comparison ranks
    parcel_df = df.reset_index().set_index('parcel')

    # Drop any ensembles across sizes
    parcel_df = parcel_df.drop(parcel_df[['-' in i and ('voted' in i or 'stacked' in i)
                                          for i in parcel_df.index]].index)
    
    # Compute ranks per target, then get means
    ranks = parcel_df.groupby(['target']).apply(get_rank_model_order)
    mean_ranks = ranks.groupby(['model', 'parcel']).apply(mean_rank)
    
    # Get as df
    scores = mean_ranks.to_frame()
    
    # Add raw r2 and roc auc
    split_means = parcel_df.groupby(['is_binary', 'model', 'parcel']).apply(mean_score)
    regression_means = split_means.loc[0]
    binary_means = split_means.loc[1]
    scores['r2'] = regression_means
    scores['roc_auc'] = binary_means
    
    # Reset index
    scores = scores.reset_index()

    # Change names
    scores = scores.rename(columns={0: 'Mean_Rank',
                                    'model': 'Model',
                                    'parcel': 'Parcellation'})

    # Add size
    scores['Size'] = [parc_sizes[p] for p in scores['Parcellation']]
    
    # Use model / strategy as index
    scores = scores.set_index('Model')
    
    return scores

def clean_name(parc):
    
    base = parc.split('/')[-1]
    name = base.replace('_', ' ').replace('.npy', '')
    name = name.replace('-', ' ')
    name = name.replace('vol resamp ', '').replace(' prob', '')
    name = name.replace(' abox', ' (abox)').replace(' dlab', ' (dlab)')
    
    return name

def clean_model_names(df):
    return df.replace({'lgbm': 'LGBM',
                       'lgbmFS': 'LGBM FS',
                       'elastic': 'Elastic-Net',
                       'elasticFS': 'Elastic-Net FS',
                       'svm':'SVM', 'all': 'All',
                       'existing': 'Existing'})

def rep_target(i):
    
    for key in target_map:
        i = i.replace(key, target_map[key])
    return i 

def target_to_name(df, are_cols=False):

    if are_cols:
        df = df.rename(target_map, axis=1)
        return df

    df['target'] = df['target'].apply(rep_target)
    return df

