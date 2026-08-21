from sklearn.datasets import make_blobs
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.datasets import make_moons
from sklearn.cluster import DBSCAN
import matplotlib.pyplot as plt

X, _ = make_blobs(n_samples=5000, centers=5, random_state=10)
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)


plt.scatter(X_scaled[:, 0], X_scaled[:, 1])
kmeans = KMeans(n_clusters=5)
kmeans.fit(X_scaled)
plt.scatter(X_scaled[:, 0], X_scaled[:, 1], c=kmeans.labels_)

      
'''
X, _ = make_moons(n_samples=5000, noise=0.01)
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
plt.scatter(X_scaled[:, 0], X_scaled[:, 1])
kmeans = KMeans(n_clusters=2)
kmeans.fit(X_scaled)
plt.scatter(X_scaled[:, 0], X_scaled[:, 1], c=kmeans.labels_)'''

'''
dbscan = DBSCAN(eps=0.2)
dbscan.fit(X_scaled)
plt.scatter(X_scaled[:, 0], X_scaled[:, 1], c=dbscan.labels_)

'''

plt.show()                                            