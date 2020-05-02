import numpy as np
"""
tanh = np.tanh
tanh_derivative = lambda x:(1-np.power(np.tanh(x),2)
sigmoid = lambda x:1/(1+np.exp(-x))
sigmoid_derivative = lambda x:sigmoid(x)*(1-sigmoid(x))
relu = lambda x:max(0,x)
relu_derivative = lambda x:(x>0)
leaky_relu = lambda x,a=10:max(x/a,x)
#leaky_relu_derivative = (lambda x,a=10:1 if x>0 else 1/a)
"""



class Layer:
    @classmethod
    def random(cls, nx, ny, f):
        w = np.random.randn(nx, ny)
        b = np.random.randn(ny, 1)
        z = np.zeros_like(b)
        return cls(w, b, a, f)
    def __init__(w, b, a, f=relu, fd=relu_derivative):
        self.w = w
        self.b = b
        self.z = z
        self.f = f
        self.fd = fd

class Model:
    @classmethod
    def random(cls, sizes, **kwargs):
        w = [np.random.randn(s1)]
        b = [np.random.randn(s,1) for s in sizes[1:])]
        z = [np.zeros((s,1)) for s in sizes[1:])]
        return cls(w, b, z, **kwargs)

    def __init__(self, w, b, z, l, f):
        self.w = w #weights
        self.b = b #biases
        self.z = z #weighted sums
        self.l = l #learning_rate
        self.f = f #activation functions

    @property
    def m(self):
        return self.w[0].shape[0]

    @property
    def s(self):
        self.s = [w.shape[1] for w in self.w] + [self.w[-1].shape[0]]

    @property
    def n(self):
        return len(self.b)

    def predict(x):
        """Return predicted output given x"""
        a = x
        for i in range(self.n):
            f = self.[i]
            w = self.w[i]
            b = self.b[i]
            z = np.dot(w, a) + b
            a = f(z)
        return a



    def forward_propagation(self, x):
        """Return predicted output given x and stores cache for backward
        propagation."""
        a = x
        for i in range(self.n):
            f = self.[i]
            w = self.w[i]
            b = self.b[i]
            z = np.dot(w, a) + b
            self.z[i] = z
            a = f(z)
        return a


    def backward_propagation(self,y,a):
        dz = a-y
        for i in range(self.n):
        

    def fit(self, x_train, y_train):

