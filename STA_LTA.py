import numpy as np

def STA(data, N):
    data_short = data[(len(data)-N):len(data)]
    return np.divide( np.sum(np.square(data_short)),N )

def LTA(data, M):
    return np.divide( np.sum(np.square(data)), M )

# need to adjust the ARL with long window length
def STA_LTA(data, tau, M, N, threshold):
    for i in range(len(data)-M):
        data_temp = data[i:M+i]
        sta = STA(data_temp, N)
        lta = LTA(data_temp, M)
        R = np.divide(sta,lta)
        if (R > threshold) and (i>(tau-M)):
            return i
        elif i==len(data)-M-1:
            return i