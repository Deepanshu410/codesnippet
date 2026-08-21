from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split

data = load_iris()
X, y = data.data, data.target
#train_test_split(X, y, test_size=0.2) # text_size=0.2 = 20% testing, 80% training
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# the data chosen for testing and training is random, which is not necessarily optimal, which can be visualized as follows;

import numpy as np
import matplotlib.pyplot as plt
'''counts = np.bincount(y_train) # counts the occurrences of non-negative integers in an array and then splits them into groups/classes.
positions = np.arange(3)
plt.bar(positions, counts)
plt.xticks(positions, data.target_names)
plt.show()
'''
# to fix this:

from sklearn.model_selection import StratifiedShuffleSplit # same distribution;guarentees having the same ratio of the different classes in the training and testing data set. 
split = StratifiedShuffleSplit(n_splits=1, test_size=0.2)
for train_idx, test_idx in split.split(X, y):
    X_train, X_test = X[train_idx], X[test_idx]
    y_train, y_test = y[train_idx], y[test_idx]

# one line alternative; 
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, stratify=y)
# test_size=0.2 handles the 80/20 data split rule.stratify=y replaces the StratifiedShuffleSplit logic. It tells the function to look at the answer key y and guarantee the train and test splits get the same class proportions.

counts = np.bincount(y_train)
positions = np.arange(3)
plt.bar(positions, counts)
plt.xticks(positions, data.target_names)
plt.show()
