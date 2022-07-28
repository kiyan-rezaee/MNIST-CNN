import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Flatten, Conv2D, MaxPool2D, Dense, ZeroPadding2D
from tensorflow.keras.utils import to_categorical
import matplotlib.pyplot as plt

x_train = np.load('x_train.npy')
x_test = np.load('x_test.npy')
y_train = np.load('y_train.npy')
y_test = np.load('y_test.npy')

# normalization
x_train = x_train / 255
x_test = x_test / 255

# expand dimension
x_train = np.expand_dims(x_train, axis=3)
x_test = np.expand_dims(x_test, axis=3)

# print(x_train[5000])

# model

model = Sequential([
    ZeroPadding2D(padding=(1, 1), input_shape=(28, 28, 1)),
    Conv2D(32, 3, activation='relu'),
    MaxPool2D(pool_size=2, strides=2),
    ZeroPadding2D(padding=(1, 1)),
    Conv2D(64, 3, activation='relu'),
    MaxPool2D(pool_size=2, strides=2),
    Flatten(),
    Dense(128, activation='relu'),
    Dense(10, activation='softmax'),
])

print(model.summary())
model.compile('adam', loss='categorical_crossentropy', metrics=['accuracy'])

# one hot encode targets
y_train_encode = to_categorical(y_train)
y_test_encode = to_categorical(y_test)

md = model.fit(x_train, y_train_encode, epochs=10, validation_data=(x_test, y_test_encode), batch_size=300)

# plot result


plt.plot(md.history['accuracy'], color='green', label='Train Data')
plt.plot(md.history['val_accuracy'], color='blue', label='Validation Data')

plt.plot(md.history['loss'], color='green', label='Train Data')
plt.plot(md.history['val_loss'], color='blue', label='Validation Data')

