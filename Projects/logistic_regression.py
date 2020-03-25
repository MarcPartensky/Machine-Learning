import numpy as np

class LogisticRegression:
    @staticmethod
    def normalize(x):
        return x/np.linalg.norm(x)

    @classmethod
    def zero(cls, size, **kwargs):
        w = np.zeros((size, 1))
        b = np.zeros((size,))
        return cls(w, b, **kwargs)

    @classmethod
    def random(cls, size, **kwargs):
        w  = np.random.randn(size, 1)
        b = np.random.randn(size)



    def __init__(self, w, b, l, i, l):
        self.w = w
        self.b = b
        self.l = l
        self.i = i

    def backprop(self, ):

    def predict(self):


    def fit(self, x_train, y_train):


    def optimize(self):

