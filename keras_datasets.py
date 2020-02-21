from keras.datasets import boston_housing,\
    mnist,\
    cifar10,\
    imdb
(x_train,y_train),(x_test,y_test)=mnist.load_data()
(x_train2,y_train2),(x_test2,y_test2)=boston_housing.load_data()
(x_train3,y_train3),(x_test3,y_test3)=cifar10.load_data()
(x_train4,y_train4),(x_test4,y_test4)=imdb.load_data(num_words=20000)
num_classes=10