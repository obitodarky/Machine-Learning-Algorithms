import matplotlib.pyplot as plt
import numpy as np
from sklearn.datasets import make_blobs


x,y = make_blobs(random_state=42)
print(x.shape)

plt.figure()
plt.scatter(x[:,0],x[:,1])


from sklearn.cluster import KMeans

kmeans = KMeans(n_clusters = 3, random_state = 42)

labels =  kmeans.fit_predict(x)

print(labels)

print(all(y == labels))

plt.figure()
plt.scatter(x[:,0],x[:,1], c = labels)

plt.figure()
plt.scatter(x[:,0] , x[:,1] , c = y )

from sklearn.metrics import confusion_matrix, accuracy_score

print('Accuracy Score : ', accuracy_score(y, labels))
print(confusion_matrix(y, labels))


np.mean(y == labels)

from sklearn.metrics import adjusted_rand_score

adjusted_rand_score(y , labels)

kmeans = KMeans(n_clusters = 2 , random_state = 42)

labels = kmeans.fit_predict(x)

plt.figure()
plt.scatter(x[:,0] , x[:,1], c = labels)

# elbow method

distortions = []

for i in range(1, 12):
    km = KMeans(n_clusters=i, random_state=0)
    km.fit(x)
    distortions.append(km.inertia_)


plt.figure()
plt.plot(range(1, 12), distortions, marker='o')
plt.xlabel('Number of clusters')
plt.ylabel('distortion')

plt.show()

X , Y = make_blobs(random_state = 170 , n_samples = 600)
rng = np.random.RandomState(74)

transformation = rng.normal(size = (2,2))

X = np.dot(X , transformation)

y_pred = KMeans(n_clusters = 3).fit_predict(X)


plt.figure()
plt.scatter(X[:,0] , X[:, 1] , c = y_pred)