import numpy as np


def equalize_3d_axes(ax, data):

    assert data.shape[0] == 3

    radius = np.array([u.max() - u.min() for u in data]).max() / 2.0
    midpoint = [(u.max() + u.min()) * 0.5 for u in data]
    limits = [(m - radius, m + radius) for m in midpoint]

    ax.set_xlim(limits[0])
    ax.set_ylim(limits[1])
    ax.set_zlim(limits[2])
