import AIC, CUSUM
import numpy as np
import Utilities
from multiprocessing import Pool

def get_ARL(func, type, repeated_times, Max_RL, tau, shift, *args, re="value"):
    data_online = Utilities.generate_all_data(type, Max_RL, repeated_times, tau, shift)
    args = [(data_online[i],*args) for i in range(repeated_times)]
    #args = [(data_online[0],Max_RL,M,m,tau,q_lists[0],d,k,r,h) for i in range(repeated_times)]
    with Pool() as pool:
        L = pool.starmap(func, args)
    if re == "value":
        return ( np.nanmean(L), np.nanstd(L)/np.sqrt(len(L)) )
    elif re == "list":
        return L
    

def get_ARLs(func_dict, type, repeated_times, Max_RL, tau, delta_list, args_2_func, re="value"):
    ARLs = dict()
    for func in func_dict:
        ARLs[func] = dict()
        for delta in delta_list:
            stat = get_ARL(func_dict[func], type, repeated_times, Max_RL, tau, delta, *args_2_func[func])
            if re == 'value':
                mean, std = round(stat[0],3), round(stat[1],3)
                ARLs[func][delta] = f'{mean} ({std})'
            elif re == 'list':
                ARLs[func][delta] = stat
    return ARLs