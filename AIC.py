import numpy as np

def aic_k(data, k, M):
    aics = list()
    aic = (k-M)*np.log(np.std(data[1:k])) + (len(data)-M-k)*np.log(np.std(data[k+1:len(data)]))
    return aic

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

def aic_precise(data, M):
    aics = aic_all(data, M)
    aics = np.nan_to_num(aics)
    return (np.min(aics), np.argmin(aics))