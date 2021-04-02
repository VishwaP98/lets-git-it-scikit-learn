# Hi everyone!!!
from random import randint

class BisectingKMeans():
    def __init__(self, max_n_clusters):
       self.max_n_clusters = max_n_clusters # num of clusters
       self.labels = None  # np array which stores the cluster info of each data point
       self.centroids = np.zeros(max_n_clusters) # np array which stores the center location of each cluster
       self.scores = np.zeros(max_n_clusters) # np array which stores the cost of each cluster

    def _next_cluster_to_split(self):
        """
        check self.clusters
        the cluster with the lowest score will the next cluster to split
        return the next cluster (label) to split
        :return:
        """
        
        minScore = float('inf')
        cluster = 0
        print(self.scores)
        for i in range(0, len(self.scores)):
            if minScore > self.scores[i]:
                minScore = self.scores[i]
                cluster = i
                
        return cluster
         
       
    def _set_cluster_location(self, labelIndex, X, isFirst=False):
        """
            Set the cluster location for the cluster with label value
            
            Parameters:
            
            labelIndex: int (3)
            
            DataSet
            X: [[a1,,,.....,a5,a6,...,an], [b1,b2,b3...,bn], .... [n1,n2,n3,...,nn]] 
            
            isFirst: default False
            
            use findRandomRow in this function

            Return:
            updated self.centroids for the label X

        """
        #Select a random point from the data points as a cluster location
        #add to self.centroids

        cordinate = []
        #NOTE: Assuming each labelIndex comes in order
        if isFirst:
            value = randint(0, len(X)-1)
            cordinate = X[value]
        # randompoint = select random from DataSet
            #generate integer from 0 to len(dataset)
            #get the coordinate at the integer generated
            #this is the randompoint
        #set the first index of the clusters to randompoint
        else:
            dimension_size = len(X[0])
            for i in range(0, dimension_size):
                value = randint(0, 1000000) #todo: what is the coordinate boundary?
                cordinate.append(value)
            
            #labeindex is the start of a new cluster
            # any random cordinate
            #append to clusters
        self.centroids[labelIndex] = cordinate
        #current state
            #Centroids: [[3,2],[5,6]] ---- this function is going to set this (we assume its not done yet)
            #Lables: [0, 0, 1, 1] --- 2 clusters             
            #dataset: [[1,2],[3,4],[5,6],[7,8]]

            #_set_cluster_location()
    
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
   
    def set_cluster_cost(self, cluster, X):
        """
        Set the cluster cost for the cluster with label value
        """
        
        # check what they did in kmeans, the cost function should have been implemented
        # you only need to update the self.scores here
        print(cluster)
        center = self.centroids[cluster]
        cost = 0
        count = 0.0
        
        for i in range(0, len(self.labels)):
            if self.labels[i] == cluster:
                
                cost += self.inertia_cost(X[i], center)
                count+=1.0
        print("cost", cost)
        print(cost/count)
        self.scores[cluster] = float(cost/count)
