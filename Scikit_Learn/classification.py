from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
X, y = load_breast_cancer(return_X_y=True)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.fit_transform(X_test)
from sklearn.neighbors import KNeighborsClassifier
# alternatives of KNeighboursClassifier; 
# from sklearn.tree import DecisionTreeClassifier
# from sklearn.linear_model import LogisticRegression
# from sklearn.svm import SVC # this doesn't have a .predict_proba
# from sklearn.ensemble import RandomForestClassifer
# from sklearn.naive_bayes import GaussianNB

clf = KNeighborsClassifier()
clf.fit(X_train_scaled, y_train)
print(clf.score(X_test_scaled, y_test)) # to check how well does the classifer does 
single_instance = X_test_scaled[1]
clf.predict([single_instance])
print(y_test[1])
print(clf.predict_proba([single_instance])) # to check measure of certainty [[20%. 80%]]