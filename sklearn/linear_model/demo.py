import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import SGDClassifier
from sklearn.datasets import make_blobs

# we create 50 separable points
X, Y = make_blobs(n_samples=1000, centers=2, random_state=0, cluster_std=0.60)

# fit the model
clf = SGDClassifier(loss="hinge", alpha=0.01, max_iter=20, verbose=1, batch_size=100)

clf.fit(X, Y)


# print("---------------------------")
# clf = SGDClassifier(loss="hinge", alpha=0.01, max_iter=200, verbose=1, batch_size=10000)

# clf.fit(X, Y)

# print("-----------------")
# clf = SGDClassifier(loss="hinge", alpha=0.01, max_iter=1, verbose=1, batch_size=10000000)

# clf.fit(X, Y)