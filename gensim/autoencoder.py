from keras.layers import Input, Dense
from keras.models import Model

from keras.datasets import mnist

(x_train, _), (x_test, _) = mnist.load_data()

encoding_dim = 32

input_img = Input(shape=(784,))

encoded = Dense(encoding_dim, activation='relu')(input_img)

decoded = Dense(784, activation='sigmoid')(encoded)

autoencoder = Model(input_img, decoded)

encoder = Model(input_img, decoded)

encoded_input = Input(shape=(encoding_dim,))

decoder_layer = encoder.layers[-1]

decoder = Model(encoded_input, decoder_layer(encoded_input))

autoencoder.compile(optimizer="adadelta", loss="binary_crossentropy")

x_train = x_train.astype('float32') / 255.
x_test = x_test.astype('float32') / 255.


