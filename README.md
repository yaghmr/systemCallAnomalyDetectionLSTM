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
```python
_________________________________________________________________
Layer (type)                 Output Shape              Param #
=================================================================
lstm_1 (LSTM)                (None, 19, 64)            103936
_________________________________________________________________
dropout_1 (Dropout)          (None, 19, 64)            0
_________________________________________________________________
lstm_2 (LSTM)                (None, 19, 256)           328704
_________________________________________________________________
dropout_2 (Dropout)          (None, 19, 256)           0
_________________________________________________________________
lstm_3 (LSTM)                (None, 100)               142800
_________________________________________________________________
dropout_3 (Dropout)          (None, 100)               0
_________________________________________________________________
dense_1 (Dense)              (None, 341)               34441
_________________________________________________________________
activation_1 (Activation)    (None, 341)               0
=================================================================
Total params: 609,881
Trainable params: 609,881
Non-trainable params: 0
_________________________________________________________________
```
Done Training...

