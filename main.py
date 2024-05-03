# K-means

# visual tasvirlash uchun matplotibpyplot kutubxonasi ishlatildi

import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

x = [1, 1, 2, 2, 6, 7, 7, -3]
y = [1, 2, 1, 2, 7, 6, 7, -4]

data = list(zip(x, y))
print(data)

inertias = []

for i in range(1, 9):
    kmeans = KMeans(n_clusters=i)
    kmeans.fit(data)
    inertias.append(kmeans.inertia_)

plt.plot(range(1, 9), inertias, marker='o')
plt.title('Elbow method')
plt.xlabel('Number of clusters')
plt.ylabel('Inertia')
plt.show()

kmeans = KMeans(n_clusters=3)
kmeans.fit(data)
plt.scatter(x, y, c=kmeans.labels_)
plt.show()
