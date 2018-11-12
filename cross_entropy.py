# Takes two ndarrays, returns the cross entropy.

def cross_entropy(Y, P):
    return -(Y * np.log(P) + (1 - Y) * np.log(1 - P)).sum()
    
