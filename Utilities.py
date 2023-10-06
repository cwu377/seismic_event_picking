import numpy as np
import pickle

def generate_all_data(type, max_len, repeated_times, tau, shift):
    if tau>max_len:
        raise ValueError("tau should not be larger than size")
    if type == 'norm':
        data = np.random.normal(0,1, size=(repeated_times, max_len))
        if shift == 0:
            pass
        elif shift != 0:
            data[:,tau:max_len] = np.random.normal(shift,1, size=(repeated_times, max_len-tau))
    return data

def serialize(d, filename):
    # Store data (serialize)
    with open(filename, 'wb') as handle:
        pickle.dump(d, handle, protocol=pickle.HIGHEST_PROTOCOL)

def deserialize(filename):
    # Store data (serialize)
    with open(filename, 'rb') as handle:
        d = pickle.load(handle)
    return d
    