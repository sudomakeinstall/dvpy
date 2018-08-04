# System

# Third Party
import numpy as np

# Internal


def normalize_image(x, mu=None, sd=None):
    if mu is None:
        mu = np.mean(x)
    if sd is None:
        sd = np.std(x)
    return (x - mu) / sd
