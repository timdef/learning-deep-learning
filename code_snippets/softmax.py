# Take a list of numbers, return list of values given by softmax function
def softmax(L):
    return np.exp(L) / np.exp(L).sum()
