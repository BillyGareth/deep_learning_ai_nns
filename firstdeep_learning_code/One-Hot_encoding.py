from keras.utils import to_categoricals
Y_train=to_categoricals(Y_train,num_classes)
Y_test=to_categoricals(Y_test,num_classes)
Y_train3=to_categoricals(Y_train3,num_classes)
Y_test3=to_categoricals(Y_test3,num_classes)