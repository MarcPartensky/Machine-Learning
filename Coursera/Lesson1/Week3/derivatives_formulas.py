"""
Formulas for computing derivatives:

Forward Propagation
a[0] = x
...
z[i] = w[i]*a[i-1]+b[i]
a[i] = g(z[i])
...
y_hat = a[n] 

Back Propagation (with mistakes)
dz[n] = a[n]-Y
dw[n] = 1/m*dz[n]*a[n].T
db[n] = 1/m*np.sum(dz[n], axis=1, keepdims=True)
...
dz[i-1] = w[i].T*dz[i] *(element wise) g'[i](z[i])
dw[i-1] = 1/m*dz[i-1]*a[i-1].T
db[i-1] = 1/m*np.sum(dz[i-1], axis=1, keepdims=True)
...
dz[1] = w[2].T*dz[2] *(element wise) g'[2](z[2])
dw[1] = 1/m*dz[1]*a[1].T
db[1] = 1/m*np.sum(dz[1], axis=1, keepdims=True)
"""


"""True version"""
dZ2 = A2-Y
dW2 = np.dot(dZ2, A1.T)/m
db2 = np.sum(dZ2,axis=1,keepdims=True)/m
dZ1 = np.dot(W2.T,dZ2)*(1-np.power(A1,2))
dW1 = np.dot(dZ1, X.T)/m
db1 = np.sum(dZ1,axis=1,keepdims=True)/m
