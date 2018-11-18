# Activation (sigmoid) function
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

# Output (prediction) formula
def output_formula(features, weights, bias):
    features.dot(weights) + bias
    return sigmoid(features.dot(weights) + bias)

# Error (log-loss) formula
def error_formula(y, output):
    return -y * np.log(output) - (1 - y) * np.log(1 - output)

# Gradient descent step
def update_weights(x, y, weights, bias, learnrate):
    output = output_formula(x, weights, bias)
    der_error = -(y - output)
    weights -= learnrate * der_error * x
    bias -= learnrate * der_error
    return weights, bias

# train(X, y, epochs, learnrate, True)
