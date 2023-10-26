import numpy as np

def STA(data, N):
    data_short = data[(len(data)-N):len(data)]
    return np.divide( np.sum(np.square(data_short)),N )

def LTA(data, M):
    return np.divide( np.sum(np.square(data)), M )

def STA_LTA(data, M, N, threshold):
    for i in range(len(data)):
        data_temp = data[i:M+i]
        sta = STA(data_temp, N)
        lta = LTA(data_temp, M)
        R = np.divide(sta,lta)
        if R > threshold:
            return i
        elif i==len(data)-1:
            return i