#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
import h5py
import numpy as np
from keras.layers.core import Dense, Activation, Dropout
from keras.layers.recurrent import LSTM
from keras.models import Sequential
from keras.models import model_from_json

import preprocess

# Global hyper-parameters
sequence_length = 19
epochs = 1
batch_size = 50
feature_dimension = 341


def read_hdf5(path):
    weights = {}
    keys = []
    with h5py.File(path, 'r') as f: # open file
        f.visit(keys.append) # append all keys to list
        for key in keys:
            if ':' in key: # contains data if ':' in key
                print(f[key].name)
                weights[f[key].name] = f[key].value
    return weights


def save_model_weight_into_file(model, modelname="model.json", weight="model.h5"):
    model_json = model.to_json()
    with open(modelname, "w") as json_file:
        json_file.write(model_json)
    # serialize weights to HDF5
    model.save_weights(weight)
    print("Saved model to disk in {} and {}".format(modelname, weight))


def load_model_and_weight_from_file(modelname="model.json", weight="model.h5"):
    json_file = open(modelname, 'r')
    loaded_model_json = json_file.read()
    json_file.close()
    loaded_model = model_from_json(loaded_model_json)
    # load weights into new model
    loaded_model.load_weights(weight)
    print("Loaded model from disk, you can do more analysis more")

    pass

def build_model():
    model = Sequential()
    layers = {'input': feature_dimension, 'hidden1': 64, 'hidden2': 256, 'hidden3': 100, 'output': feature_dimension}

    model.add(LSTM(
        input_length=sequence_length,
        input_dim=layers['input'],
        output_dim=layers['hidden1'],
        return_sequences=True))
    model.add(Dropout(0.2))

    model.add(LSTM(
        layers['hidden2'],
        return_sequences=True))
    model.add(Dropout(0.2))

    model.add(LSTM(
        layers['hidden3'],
        return_sequences=False))
    model.add(Dropout(0.2))

    model.add(Dense(
        output_dim=layers['output'],
        activation='softmax'))
    #model.add(Activation("linear"))

    start = time.time()

    model.compile(loss="categorical_crossentropy", optimizer='rmsprop', metrics=['accuracy'])
    #model.compile(loss="mse", optimizer="rmsprop")

    print("Compilation Time : ", time.time() - start)
    return model


def run_network(model=None):

    global_start_time = time.time()

    print('Loading data... ')
    X_train, y_train = preprocess.preprocess('train')
    X_test, y_test = preprocess.preprocess('test')

    print("X_train, y_train,shape")
    print(X_train.shape)
    print(y_train.shape)
    print('\nData Loaded. Compiling...\n')

    if model is None:
        model = build_model()

    try:
        print("Training...")
        model.fit(
            X_train, y_train,
            batch_size=batch_size,
            epochs=epochs,
            validation_split=0.05)
        model.summary()
        print("Done Training...")

        predicted = model.predict(X_test)
        print("Reshaping predicted")
        predicted = np.reshape(predicted, (predicted.size,))

    except KeyboardInterrupt:
        print("prediction exception")
        print('Training duration (s) : ', time.time() - global_start_time)
        return model, y_test, 0

    print('Training duration (s) : ', time.time() - global_start_time)

    save_model_weight_into_file(model)

    return model, y_test, predicted


if __name__ == "__main__":
    run_network()
    #print(read_hdf5('model.h5'))
