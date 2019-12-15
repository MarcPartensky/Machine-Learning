from keras.layers import Dense, Input
from keras.models import Model
from keras.datasets import mnist
from keras.callbacks import TensorBoard

(x_train, _), (x_test, _) = mnist.load_data()

input_img = Input(shape=(784,))

x = Dense(128, activation='relu')(input_img)
x = Dense(64, activation='relu')(x)
encoded = Dense(10, activation='relu')(x)

x = Dense(64, activation='relu')(encoded)
x = Dense(128, activation='relu')(x)
decoded = Dense(784, activation='sigmoid')(x)

coder = Model(input_img, encoded)
# decoder = Model(encoded, decoded)
autoencoder = Model(input_img, decoded)

autoencoder.compile(optimizer='adadelta', loss='binary_crossentropy')

autoencoder.fit(x_train, x_train,
                epochs=100,
                batch_size=256,
                shuffle=True,
                validation_data=(x_test, x_test),
                callbacks=[TensorBoard(log_dir="/tmp/autoencoder")])





