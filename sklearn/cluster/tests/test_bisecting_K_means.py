import numpy as np
from numpy.testing import (assert_equal,assert_array_equal)
import pytest
from sklearn.cluster import BisectingKMeans


@pytest.mark.parametrize("scores", [[1, 99, 32.45], [0.77,0.5, 0], [100.99, 34.89, 8000], []])
def test_next_cluster_to_split(scores):
    bisectingKMeans = BisectingKMeans()
    bisectingKMeans.scores = np.array(scores)
    assert_equals(bisectingKMeans._next_cluster_to_split(), scores.index(min(scores)))


'''
@pytest.mark.parametrize('X, labels, centroids, scores', [([[1],[2],[3],[4],[5],[6],[7],[8],[10]], 
[[0,0,0,1,1,1,2,2,2]], [[0,0,0]], [[2.0, 2.0, 4.0]])])
def test_set_cluster_location(X, labels, centroids, scores):
'''

   

@pytest.mark.parametrize('X, labels, centroids, scores', [([[1],[2],[3],[4],[5],[6],[7],[8],[10]], 
[[0,0,0,1,1,1,2,2,2]], [[0,0,0]], [[2.0, 2.0, 4.0]])])
def test_set_cluster_cost(X, labels, centroids, scores):
    bisectingKMeans = BisectingKMeans()
    bisectingKMeans.scores = np.array(scores)
    assert_equals(bisectingKMeans._next_cluster_to_split(), scores.index(min(scores)))

    X = np.array(X)
                
    clf = BisectingKMeans(max_n_clusters=2)

    clf.labels = np.array(labels)
    clf.centroids = np.array(centroids)
    clf.scores = np.array(scores)

    z = clf.set_cluster_cost(0, X)
    assert_array_equal(z, [0.666666, 2.0, 4.0])