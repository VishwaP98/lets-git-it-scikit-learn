from random import randint
import numpy as np

class BisectingKMeans():
    def __init__(self, max_n_clusters):
       self.max_n_clusters = max_n_clusters # num of clusters
       self.labels = None  # np array which stores the cluster info of each data point
       self.centroids = np.zeros(max_n_clusters) # np array which stores the center location of each cluster
       self.scores = np.zeros(max_n_clusters) # np array which stores the cost of each cluster

    def _next_cluster_to_split(self):
        """
        Returns the next cluster to split based on the scores for each cluster
        """
        
        max_score = 0.0
        cluster = 0
        for i in range(0, len(self.scores)):
            if max_score < self.scores[i]:
                max_score = self.scores[i]
                cluster = i
                
        return cluster

    
    def inertia_cost(self, x1, x2):
        '''
        >>> inertia_cost([1, 0, 1], [0, 1, 1])
            2
        '''
        inertia = 0
        print("x1", x1)
        print("x2", x2)
        for a, b in zip(x1, x2):
            inertia += (a - b)**2
        return inertia