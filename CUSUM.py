import numpy as np


def cusum_stat(Sn, Zn1, w, sign="+"):
    if sign == "+":
        return np.max([0, Sn + Zn1 - w])
    elif sign == "-":
        return np.max([0, Sn - Zn1 - w])
    else:
        raise ValueError("sign should be in {+,-}")


def cusum(X, tau, mean, sigma, w, threshold):
    Z = ( X-mean )/sigma
    Sh = 0
    Sl = 0
    for i in range(len(X)):
        Sh = cusum_stat(Sh, Z[i], w, "+")
        Sl = cusum_stat(Sl, Z[i], w, "-")
        S = np.max([Sh,Sl])
        if (S > threshold) and (i>tau):
            return (i-tau)
        if i==(len(X)-1):
            return (i-tau)
        
def cusum_stat_vec(Sn, Zn1, w, sign="+"):
    l = Sn.shape[0]
    if sign == "+":
        return np.max([np.zeros(l), Sn + Zn1 - w], axis=0)
    elif sign == "-":
        return np.max([np.zeros(l), Sn - Zn1 - w], axis=0)
    else:
        raise ValueError("sign should be in {+,-}")
        
def cusum_vec(X, tau, mean, sigma, w, threshold):
    Z = (X-mean)/sigma
    l = X.shape[0]
    Sh = np.zeros(l)
    Sl = np.zeros(l)
    for i in range(X.shape[1]):
        Sh = cusum_stat_vec(Sh, Z[:,i], w, "+")
        Sl = cusum_stat_vec(Sl, Z[:,i], w, "-")
        S = np.max([Sh,Sl], axis=0)
        S = -np.sort(-S)
        top_r = np.sum(S[0:5])
        if (top_r > threshold) and (i>tau):
            return (i-tau)