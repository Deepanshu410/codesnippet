# Principle component analysis
from sklearn.datasets import fetch_openml
from sklearn.decomposition import PCA
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
import numpy as np

X, y = fetch_openml('mnist_784', return_X_y=True)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)
pca = PCA(n_components=10)
X_train_reduced = pca.fit_transform(X_train)
X_test_reduced = pca.transform(X_test)
print(X_train.shape) # original shape
print(X_train_reduced.shape) # reduced shape
'''clf = LogisticRegression(max_iter=100)
clf.fit(X_train, y_train)
print(clf.score(X_test, y_test))'''
clf = LogisticRegression(max_iter=100)
clf.fit(X_train_reduced, y_train)
print(clf.score(X_test_reduced, y_test))
print(np.sum(pca.explained_variance_ratio_)) # It tells you exactly how much "information" or variation is retained when you reduce your data from the original features to the new principal components.