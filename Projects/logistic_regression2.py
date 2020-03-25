import numpy as np


class LogisticRegression:
    @staticmethod
    def normalize(x):
        return x / np.linalg.norm(x)

    @classmethod
    def zero(cls, size, **kwargs):
        weight = np.zeros((size, 1))
        bias = 0
        return cls(weight, bias, **kwargs)

    @classmethod
    def random(cls, size, **kwargs):
        weight = np.random.randn(size, 1)
        bias = np.random.random(size)
        return cls(weight, bias, **kwargs)

    def __init__(self, weight, bias, learning_rate=0.01, iterations=1e3):
        self.weight = weight
        self.bias = bias
        self.learning_rate = learning_rate
        self.iterations = iterations

    @property
    def w(self):
        return self.weight

    @w.setter
    def w(self, weight):
        self.weight = weight

    @w.deleter
    def w(self):
        del self.weight

    wAlias = w

    @property
    def b(self):
        return self.bias

    @b.setter
    def b(self, bias):
        self.bias = bias

    @b.deleter
    def b(self):
        del self.bias

    @property


    # b = super.bias
    # l = super.learning_rate
    # i = super.iterations

    def train(self, x_train, y_train):
        pass


if __name__ == "__main__":
    m = LogisticRegression.random(10)
    print(m.wAlias)
