from __future__ import print_function

import keras
from keras.callbacks import Callback
from keras.datasets import mnist, fashion_mnist
from keras.layers import Dense, Dropout
from keras.models import Sequential
from keras.optimizers import Adam
from sacred import Experiment
from sacred.observers import MongoObserver
from sacred.stflow import LogFileWriter


class MetricLogger(Callback):
    def __init__(self, ex):
        super(MetricLogger, self).__init__()
        self.ex = ex

    def on_epoch_end(self, epoch, logs=None):
        for name, value in logs.items():
            self.ex.log_scalar(name, float(value), epoch)

ex = Experiment()
ex.observers.append(MongoObserver.create(url='mongodb://localhost:YOURPORT'))


@ex.config
def config():
    batch_size = 128
    num_classes = 10
    epochs = 5
    lr = 0.001
    dataset = 'mnist'


@ex.capture
def get_model(num_classes, lr):
    model = Sequential()
    model.add(Dense(32, activation='relu', input_shape=(784,)))
    model.add(Dropout(0.2))
    model.add(Dense(32, activation='relu'))
    model.add(Dropout(0.2))
    model.add(Dense(num_classes, activation='softmax'))
    model.summary()
    model.compile(loss='categorical_crossentropy',
                  optimizer=Adam(lr),
                  metrics=['accuracy'])
    return model


@ex.capture
def get_data(num_classes, dataset):
    # the data, shuffled and split between train and test sets
    if dataset == 'mnist':
        (x_train, y_train), (x_test, y_test) = mnist.load_data()
    elif dataset == 'fashion':
        (x_train, y_train), (x_test, y_test) = fashion_mnist.load_data()
    else:
        raise ValueError()
    x_train = x_train.reshape(60000, 784)
    x_test = x_test.reshape(10000, 784)
    x_train = x_train.astype('float32')
    x_test = x_test.astype('float32')
    x_train /= 255
    x_test /= 255
    print(x_train.shape[0], 'train samples')
    print(x_test.shape[0], 'test samples')
    # convert class vectors to binary class matrices
    y_train = keras.utils.to_categorical(y_train, num_classes)
    y_test = keras.utils.to_categorical(y_test, num_classes)
    return x_test, x_train, y_test, y_train


@ex.automain
@LogFileWriter(ex)
def run(batch_size, epochs, num_classes):
    x_test, x_train, y_test, y_train = get_data(num_classes)

    model = get_model(num_classes)

    history = model.fit(x_train, y_train,
                        batch_size=batch_size,
                        epochs=epochs,
                        verbose=2,
                        callbacks=[MetricLogger(ex)],
                        validation_data=(x_test, y_test))
    score = model.evaluate(x_test, y_test, verbose=0)
    print('Test loss:', score[0])
    print('Test accuracy:', score[1])
    return score[1]
