# -*- coding: utf-8 -*-
"""
Spyder Editor

This temporary script file is located here:
C:\Users\chrisfan\.spyder2\.temp.py
"""
import numpy as np

mydata = np.genfromtxt('C:\Users\chrisfan\Documents\GitHub\Data_Mining_Final_Project\Maps\data\knn_sklearn_data.csv', delimiter=",")
mytarget = np.genfromtxt('C:\Users\chrisfan\Documents\GitHub\Data_Mining_Final_Project\Maps\data\knn_sklearn_target.csv', delimiter=",")
np.random.seed(0)

mydata_X = mydata
mydata_Y = mytarget

indices = np.random.permutation(len(mydata_X))
mydata_X_train = mydata_X[indices[:-20]]
mydata_y_train = mydata_Y[indices[:-20]]
mydata_X_test  = mydata_X[indices[-20:]]
mydata_y_test  = mydata_Y[indices[-20:]]

from sklearn.neighbors import KNeighborsClassifier
knn = KNeighborsClassifier()
knn.fit(mydata_X_train, mydata_y_train)
knn_predict = knn.predict(mydata_X_test)
mydata_y_test

from sklearn import svm
clf = svm.SVC(gamma=0.001, C=100.)
clf.fit(mydata_X_train, mydata_y_train) 
svm_predict = clf.predict(mydata_X_test)