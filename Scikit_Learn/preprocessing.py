from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

X, y = load_iris(return_X_y=True)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# same result as; in numpy
import numpy as np
variable = (X_train - np.mean(X_train, axis=0)) / np.std(X_train, axis=0)

# alternative

from sklearn.preprocessing import minmax_scale
scaler = minmax_scale()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# above one in numpy; 
X_min = np.min(X_train, axis=0)
X_max = np.max(X_train, axis=0)
variable2 = (X_train - X_min) / (X_max - X_min)