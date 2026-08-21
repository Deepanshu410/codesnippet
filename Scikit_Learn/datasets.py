import matplotlib.pyplot as plt
import pandas as pd
from sklearn.datasets import load_breast_cancer, fetch_california_housing, fetch_openml
# load functions - provided already, fetch functions - that allow to pull data from the internet
#data = load_breast_cancer()
#X = data.data
#y = data.target 
# same as;
#X,y = load_breast_cancer(return_X_y=True)
#print(X, y)
# as pandas dataframe;
#df = load_breast_cancer(as_frame=True).frame
#print(df)

from sklearn.datasets import make_blobs, make_moons # generates data randomly according to certain distributions or structures, blobs(clusters) creates clusters of data points
X, y = make_blobs(n_samples=500, centers=5) # (n_samples = number of instances, centers= number of clusters, n_features= number of dimensions)
plt.scatter(X[:, 0], X[:, 1], c=y)
# useful for clustering methods; 
X, y = make_moons(noise=0.1, random_state=0) # make_moons() gives shape, noise=0.1 makes the shape misalingned, without random_state there would be different data everytime, and after setting there we would be consistent generations, same result.
plt.scatter(X[:, 0], X[:, 1], c=y)
plt.show()
