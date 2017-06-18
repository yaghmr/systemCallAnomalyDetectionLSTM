# xxxx

System call anomaly detection using multi-HMMs

## Dataset:
UNM system call dataset 

https://www.cs.unm.edu/~immsec/data/synth-sm.html


ADFA-LD:
https://www.unsw.adfa.edu.au/australian-centre-for-cyber-security/cybersecurity/ADFA-IDS-Datasets/


LSTM-BASED SYSTEM-CALL LANGUAGE MODELING AND ROBUST ENSEMBLE METHOD FOR DESIGNING HOST-BASED INTRUSION DETECTION SYSTEMS
https://arxiv.org/pdf/1611.01726.pdf

Idea:
char-based system call 


https://github.com/karpathy/char-rnn
char NN 


padding the sequence

https://stackoverflow.com/questions/42002717/how-should-we-pad-text-sequence-in-keras-using-pad-sequences

https://github.com/fchollet/keras/issues/1641


loss functions;

https://keras.io/losses/#categorical_crossentropy


paper:
LSTM-Based System-Call Language Modeling and Robust Ensemble Method for Designing Host-Based Intrusion Detection Systems.

## Sample code:

http://machinelearningmastery.com/time-series-prediction-lstm-recurrent-neural-networks-python-keras/


https://github.com/aurotripathy/lstm-anomaly-detect


# Run

The train data size is that
X_Train (20298, 19, 341)
Y_Train (20298, 341)

19283/19283 [==============================] - 147s - loss: 0.0024 - val_loss: 0.0022


another losses

model.compile(loss="categorical_crossentropy", optimizer="rmsprop")

19283/19283 [==============================] - 153s - loss: 10.5728 - val_loss: 8.1006


model.compile(loss="categorical_crossentropy", optimizer="sgd")

19283/19283 [==============================] - 148s - loss: 9.8008 - val_loss: 13.7872

Done Training...

