"""
Logistic Regression:

Given w, b, X, Y

m = X.shape[1]
A = sigmoid(np.dot(w.T, X) + b) # compute activation
cost = 1/m*np.sum(- np.dot(Y, np.log(A).T) - np.dot((1-Y), np.log(1-A).T))

dw = 1/m*np.dot(X,(A-Y).T)
db = 1/m*np.sum(A-Y)

cost = np.squeeze(cost)
"""
