from keras.layers import Input, Dense
from keras.models import Model
import keras.datasets.mnist as mnist

(xtrain, ytrain), (xtest, ytest) = mnist.load_data()

# this is the size of our encoded representations
encoding_dim = 32  # 32 floats -> compression of factor 24.5, assuming the input is 784 floats
sizes = [784, 400, 400, 10]

# this model maps an input to its reconstruction
coder = Model(Input(shape=(sizes[0],)),
              Dense(sizes[1], activation='relu'),
              Dense(sizes[2], activation='relu'),
              Dense(sizes[3], activation='relu'),
              Dense(sizes[4], activation='sigmoid')),
              Dense(sizes[3], activation='relu'),
              Dense(sizes[2], activation='relu'),
              Dense(sizes[1], activation='relu'),
              Dense(sizes[0], activation='sigmoid'))


decoder.fit()

