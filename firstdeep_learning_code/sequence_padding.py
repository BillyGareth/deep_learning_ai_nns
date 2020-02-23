from keras.preprocessing import sequence
x_train4=sequence.pad_sequences(x_train4,maxlen=80)
x_test4=sequence.pad_sequences(x_test4,maxlen=80)