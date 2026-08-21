from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

X, y = fetch_california_housing(return_X_y=True)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

from sklearn.linear_model import LinearRegression # alt regressions, Lasso, Ridge, ElasticNet
# alternatives;
from sklearn.neighbors import KNeighborsRegressor
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestRegressor
from sklearn.tree import DecisionTreeRegressor


reg = LinearRegression()
reg.fit(X_train_scaled, y_train)
reg.score(X_test_scaled,y_test) # R sq score
single_instance = X_test_scaled[0]
print(reg.predict([single_instance]))
