from sklearn.datasets import load_breast_cancer
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split, GridSearchCV

X, y = load_breast_cancer(return_X_y=True)
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)
param_grid = {
    'n_estimators': [50, 100, 200],
    'min_samples_split': [2, 5],
    'max_depth': [None, 5, 10]
}
clf = RandomForestClassifier(n_jobs=-1)
grid = GridSearchCV(clf, param_grid, cv=3)
grid.fit(X_train, y_train)
print(grid.best_params_)
best_clf = grid.best_estimator_
print(best_clf.score(X_test, y_test))
