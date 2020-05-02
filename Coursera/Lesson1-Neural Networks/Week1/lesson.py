"""
supervised learning:
m = number of examples = size of the data
m_train = number of training examples
m_test = number of test examples

x = input vector
y = output vector 
y_hat = predicted output vector

nx = length of the input vector
ny = length of the output vector

w = weight(s) vector(s) of the neural network
b = bias(s) vector(s) of the neural network
t_w = transpose matrix of w
z = t_w * x + b
sigmoid(z) = 1/(1+math.exp(-z))
y_hat = a = sigmoid(z)

L(y_hat,y) = loss function applied on a single example
J(w,b) = cost function = average of L given all examples

common loss function:
L(y_hat,h) = 1/2*(y-y_hat)**2
on logistic regression problems:
L(y_hat,y) = - (y*math.log(y_hat) + (1-y)*math.log(1-y_hat))
L(a,y) = - (y*math.log(a) + (1-y)*math.log(1-a))

learned about computation graph and computing derivatives that comes with it

make use of the chain rule of derivatives :
dz/dx = dz/dy * dy/dx
"""

"dvar is the derivate of the final output variable by the input variable"

"""
"da" = dL(a,y)/da = -y/a + (1-y)/(1-a)
"dz" = dL(a,y)/dz = dL/da * da/dz
"dw" = dL/dw
"db" = dL/db

to resume:
dL/dw = dL/da * da/dz * dz/dw
dL/db = dl/da * da/dz * dz/db

however we know that:
dL/da = -y/a + (1-y)/(1-a)
da/dz = a(1-a)

dz/dw = x
dz/db = 1

so:
dL/dz = a - y




"""

import numpy as np
import math


def logistic_regression(x, y, J=0, dw1=0, dw2=0, db=0,l=0.05):
	m = x.shape[0]
	z = np.zeros_like(x[0])
	w1 = random.random()
	w2 = random.random()
	b = random.random()
	for i in range(m):
		z[i] = np.dot(w, x[i]) + b
		a_i = sigmoid(z[i])
		Jt = -(y[i]*math.log(a_i) + \
			(1-y[i]) * math.log(1-a_i))
		dz_i = a_i - y[i]
		dw1 += x1_i * dz_i
		dw2 += x2_i * dz_i
		db += dz_i
	J/=m
	dw1/=m; dw2/=m; db/=m
	w1 -= l*dw1
	w2 -= l*dw2
	b -= l*db
	return [w,b]
	

		


"""
J=0 ; dw1=0; dw2=0; db=0 
for i=1 to m
	z[i] = t_w * x[i] + b
	a[i] = sigmoid(z[i])
	Jt = -[y[i]*log(a[i]) + (1-y[i])*log(1-a[i])]
	dz[i] = a[i] - y[i]
	dw1 += x1[i] * dz[i]
	dw2 += x2[i] * dz[i]
	db += dz[i]

J/=m
dw1/=m; dw2/=m; db/=m

 w1 -= l*dw1
 w2 -= l*dw2
 b -= l*db
"""


"""Vectorization:
Z = np.dot(w.T, X) + b
A = sigmoid(Z)


Implement Logistic Regression

Z = tw*X+b = np.dot(w.T,X) + b
A = sigmoid(Z)
dZ = A-Y
dW = 1/m * np.dot(X, dZ.T)
dB = 1/m* np.sum(dZ)

w -= alpha * dW
b -= alpha * dB


"""
