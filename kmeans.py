import numpy as np
import matplotlib.pyplot as plt

data = np.array([
    [1, 2],
    [10, 1],
    [2, 8],
    [10, 2],
    [9, 1],
    [1, 5],
    [4, 5],
    [8, 2]
])

def euclidean_distance(a, b):
    return np.sqrt(np.sum((a - b) ** 2))

def compute_centroid(points):
    return np.mean(points, axis=0)

def k_means(data, k=2, max_iters=100):
    # Centroid awal adalah M1 dan M5
    centroids = np.array([data[0], data[4]])
    # centroids = data[1, 5]
    for _ in range(max_iters):
        clusters = [[] for _ in range(k)]
        for point in data:
            distances = [euclidean_distance(point, centroid) for centroid in centroids]
            cluster_index = np.argmin(distances)
            clusters[cluster_index].append(point)

        new_centroids = np.array([compute_centroid(np.array(cluster)) if len(cluster) > 0 else centroids[i] for i, cluster in enumerate(clusters)])

        if np.all(centroids == new_centroids):
            break
        centroids = new_centroids

    return centroids, clusters

k = 2  
centroids, clusters = k_means(data, k)
colors = ['r', 'g', 'b']
for i, cluster in enumerate(clusters):
    cluster_np = np.array(cluster)
    plt.scatter(cluster_np[:, 0], cluster_np[:, 1], c=colors[i], label=f'Cluster {i + 1}')

centroids_np = np.array(centroids)
plt.scatter(centroids_np[:, 0], centroids_np[:, 1], c='black', marker='x', s=100, label='Centroids')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('K-Means Clustering')
plt.legend()

centroid_text = '\n'.join([f'Centroid {i + 1}: ({centroid[0]:.2f}, {centroid[1]:.2f})' for i, centroid in enumerate(centroids)])
plt.figtext(0.5, 0, centroid_text, ha='center', fontsize=10, bbox={"facecolor":"orange", "alpha":0.5, "pad":5})
plt.show()
