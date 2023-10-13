import numpy as np

def STA(data, N):
    data_short = data[N:len(data)]
    return np.sum(data_short)/N

def LTA(data):
    return np.sum(data)/len(data)

def STA_LTA(data, M, N, threshold):
    for i in range(len(data)):
        data_temp = data[i:M+i]
        sta = STA(data_temp, N)
        lta = LTA(data_temp)
        R = sta/lta
        if R > threshold:
            return i
        elif i==len(data)-1:
            return i