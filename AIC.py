import numpy as np
import warnings

def aic_k(data, k, M):
    #aic = (k-M)*np.log(std_adjust(np.std(data[1:k]))) + (len(data)-M-k)*np.log(std_adjust(np.std(data[k+1:len(data)])))
    aic = (k-2)*np.log(np.var(data[0:k])) + (len(data)-2-k)*np.log(np.var(data[k:len(data)]))
    return aic

def std_adjust(value):
    if value!=0:
        return value
    elif value == 0:
        return 0.0000000000000000000000000000000000000001

def aic(data, M):
    aics = list()
    for i in range(len(data)):
        aics.append(aic_k(data, i, M))
        if len(aics) >= 2:
            if aics[i] > aics[i-1]:
                return i
            
def aic_all(data, M):
    aics = list()
    for i in range(len(data)):
        aics.append(aic_k(data, i, M))
    return aics

def aic_precise(data, tau, M):
    with warnings.catch_warnings():
        warnings.simplefilter("ignore", category=RuntimeWarning)
        aics = aic_all(data, M)
        aics = np.nan_to_num(aics)
    return np.argmin(aics)