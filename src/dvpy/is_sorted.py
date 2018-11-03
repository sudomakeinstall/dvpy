import numpy as np


def is_sorted(l):
    return np.all([l[i] < l[i + 1] for i in range(len(l) - 1)])
