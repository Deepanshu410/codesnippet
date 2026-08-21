from sklearn.datasets import load_breast_cancer
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

# classification metric
X, y = load_breast_cancer(return_X_y=True)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.fit_transform(X_test)
'''clf = KNeighborsClassifier()
clf.fit(X_train_scaled, y_train)
print(clf.score(X_test_scaled, y_test)) # accuracy score 
# accuracy tells, out of the examples that i wanted to classify, how many did i classify correctly. Whereas, precision tells us when i say that something is true, how often am i correct. And recall would be something like how many of the correct instances would i recognize.

from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
y_pred = clf.predict(X_test_scaled)
print(accuracy_score(y_test, y_pred))
print(precision_score(y_test, y_pred))
print(recall_score(y_test, y_pred))
print(f1_score(y_test, y_pred))
'''

# Regression metric

from sklearn.datasets import fetch_california_housing
from sklearn.linear_model import LinearRegression
reg = LinearRegression()
reg.fit(X_train_scaled, y_train)
print(reg.score(X_test_scaled, y_test)) # R sq score

from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error, root_mean_squared_error

y_pred = reg.predict(X_test_scaled)
print(r2_score(y_test, y_pred)) # same as the R sq score
print(mean_absolute_error(y_test, y_pred))
print(mean_squared_error(y_test, y_pred))
print(root_mean_squared_error(y_test, y_pred))