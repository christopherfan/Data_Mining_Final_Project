# -*- coding: utf-8 -*-
"""
Spyder Editor

This temporary script file is located here:
C:\Users\chrisfan\.spyder2\.temp.py
"""
import numpy as np
from sklearn import preprocessing
from sklearn.externals.six import StringIO

mydata = np.genfromtxt('C:\Users\chrisfan\Documents\GitHub\Data_Mining_Final_Project\Maps\data\csv\knn_sklearn_data.csv', delimiter=",")
mytarget = np.genfromtxt('C:\Users\chrisfan\Documents\GitHub\Data_Mining_Final_Project\Maps\data\csv\knn_sklearn_target.csv', delimiter=",")
np.random.seed(0)

mydata_X = mydata
#mydata_X = preprocessing.normalize(mydata)
mydata_Y = mytarget

indices = np.random.permutation(len(mydata_X))
print "Dataset Totals: ", len(mydata_X)
#test_number = int(.2 * len(mydata_X) * -1)
test_number = -50
mydata_X_train = mydata_X[indices[:test_number]]
mydata_y_train = mydata_Y[indices[:test_number]]
mydata_X_test  = mydata_X[indices[test_number:]]
mydata_y_test  = mydata_Y[indices[test_number:]]

#### KNN Code
from sklearn.neighbors import KNeighborsClassifier
knn = KNeighborsClassifier()
knn.fit(mydata_X_train, mydata_y_train)
knn_predict = knn.predict(mydata_X_test)
mydata_y_test

#### SVM Code
from sklearn import svm
clf = svm.SVC(gamma=0.001, C=100.)
clf.fit(mydata_X_train, mydata_y_train) 
svm_predict = clf.predict(mydata_X_test)

#### Decision Tree Code
from sklearn import tree
clf = tree.DecisionTreeClassifier()
clf.fit(mydata_X_train, mydata_y_train) 
tree_predict = clf.predict(mydata_X_test)

print "y data", mydata_y_test

correct = 0
print "KNN Results: ", knn_predict
for entry in xrange(len(mydata_y_test)):
    if mydata_y_test[entry]== knn_predict[entry]:
        correct+=1
print "total correct", correct /float(len(mydata_y_test))


print "Tree Results: ", tree_predict
correct = 0
for entry in xrange(len(mydata_y_test)):
    if mydata_y_test[entry]== tree_predict[entry]:
        correct+=1
print "total correct", correct, correct /float(len(mydata_y_test))

from sklearn.externals.six import StringIO  
with open("iris.dot", 'w') as f:
    f = tree.export_graphviz(clf, out_file=f)
import os
os.unlink('iris.dot')    