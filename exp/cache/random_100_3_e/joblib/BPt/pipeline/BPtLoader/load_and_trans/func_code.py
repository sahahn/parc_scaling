# first line: 13
def load_and_trans(transformer, load_func, loc):
    '''This function is designed to be able to be wrapped in a cache
    check_memory.'''

    data = load_func(loc)
    trans_data = np.squeeze(transformer.fit_transform(data))
    return trans_data
