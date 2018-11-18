# Predict probability using the sigmoid function.
# Given 
w1 = 4
w2 = 5
b = -9

def sig_pred(x1,x2):
    score = w1 * x1 + w2 * x2 + b
    return 1/(1+np.exp(-score))

print("(1,1):",sig_pred(1,1))
print("(2,4):",sig_pred(2,4))
print("(5,-5):",sig_pred(5,-5))
print("(-4,5):",sig_pred(-4,5))

# Returns
# (1,1): 0.5
# (2,4): 0.9999999943972036
# (5,-5): 8.315280276641321e-07
# (-4,5): 0.5
