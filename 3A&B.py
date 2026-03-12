import numpy as np
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt


x = np.array([[15,39], [16,81], [17,6], [18,77], [19,40], [20,80]])

kmeans=KMeans(n_clusters=2)

kmeans.fit(x)

labels=kmeans.labels_
print(labels)

plt.scatter(x[:0],y[:1],c=labels,cmap='rainbow')
plt.scatter(kmeans.cluster_centers_[:,0],
                kmeans.cluster_centers_[:,1],
                color='blue',
            marker='x',
            s=200,
            label='centroid')
plt.xlabel("Annual Income")
plt.ylabel("Spending Score")
plt.legend()
plt.show()
