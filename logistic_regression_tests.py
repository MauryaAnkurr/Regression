import numpy as np
from sklearn.model_selection import train_test_split
from sklearn import datasets

# import matplotlib.pyplot as plt

from logistic_regression import LogisticRegression

bc = datasets.load_breast_cancer()
X, y = bc.data, bc.target

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=.2, random_state=1234)


def accuracy(y_true, y_pred):
    accuracy = np.sum(y_true == y_pred) / len(y_true)
    return accuracy


regressor = LogisticRegression(lr=.0001, n_iteration=100000)
regressor.fit(X_train, y_train)

predictions = regressor.predict(X_test)

print(" LR accuracy :", accuracy(y_test, predictions))
