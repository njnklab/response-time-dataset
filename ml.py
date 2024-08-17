from sklearn.metrics import classification_report, confusion_matrix
from sklearn.model_selection import train_test_split, cross_val_score, cross_val_predict
from sklearn.linear_model import LogisticRegression
from sklearn.neural_network import MLPClassifier

import pandas as pd
import numpy as np


def get_xy(data):
    print(data['label'].value_counts())
    y = data['label'].values
    x = data.filter(regex='^(time_)').values
    return x, y

def ml(X, y):
    # 10-fold cross validation
    clf = LogisticRegression()
    val_pred = cross_val_predict(clf, X, y, cv=10)
    val_proba = cross_val_predict(clf, X, y, cv=10, method='predict_proba')
    return val_pred, val_proba

