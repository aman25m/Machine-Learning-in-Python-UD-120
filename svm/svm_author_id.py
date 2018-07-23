#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 2 (SVM) mini-project.

    Use a SVM to identify emails from the Enron corpus by their authors:    
    Sara has label 0
    Chris has label 1
"""
import sys
from time import time
from sklearn import svm
sys.path.append("../tools/")
from sklearn.metrics import accuracy_score
from email_preprocess import preprocess


### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()

features_train = features_train[:len(features_train)/100]
labels_train = labels_train[:len(labels_train)/100]

clf = svm.SVC(kernel='linear')
clf.fit(features_train, labels_train)
pred = clf.predict(features_test)

acc = accuracy_score(labels_test,pred)
print acc

#rbf kernel svm
clf_rbf = svm.SVC(kernel='rbf')
clf_rbf.fit(features_train,labels_train)
pred = clf_rbf.predict(features_test)

acc = accuracy_score(labels_test,pred)
print acc

#########################################################
### your code goes here ###

#########################################################


