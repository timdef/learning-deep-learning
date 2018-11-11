# Exploring a perceptron learning rule.

def perceptronStep(X, y, W, b, learn_rate = 0.01):
    for idx in range(len(X)):
        pred = prediction(X[idx],W,b)
        if pred != y[idx]:
            if pred == 0:
                W[0] = W[0] + (X[idx][0] * learn_rate)
                W[1] = W[1] + (X[idx][1] * learn_rate)
                b += learn_rate
            elif pred == 1:
                W[0] = W[0] - (X[idx][0] * learn_rate)
                W[1] = W[1] - (X[idx][1] * learn_rate)
                b -= learn_rate
    return W, b

W = np.array([[0.37454012],[0.95071431]]) #ndarray
b = np.float64(1.731993941811405)
for i in range(30):
    W, b = perceptronStep(X, y, W, b)
    percentage_correct()
