import numpy as np
from scipy.spatial.distance import cityblock
from math import sqrt

data = [[1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1],
        [1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 1],
        [1, 1, 1, 0, 1, 3, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 1]]
def distance(row1, row2):
    return (cityblock(row1, row2))


def find_nearest_pair(data):

    N = len(data)
    dist = np.inf
    dist = np.empty((N, N), dtype=float)

    dist = [[distance(row1, row2) for row1 in data] for row2 in data]
    for i in range(len(dist)):
        dist[i][i] = np.inf

    dist = np.asarray(dist)

    print(np.unravel_index(np.argmin(dist), dist.shape))

find_nearest_pair(data)
