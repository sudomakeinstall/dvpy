# System

# Third Party
import numpy as np
from skimage.morphology import label

# Internal


def keep_largest_connected_component(image):
    if np.sum(image) == 0:
        return image
    labels, num = label(image, return_num=True)
    sums = [np.sum(labels == n) for n in range(1, num + 1)]
    label_to_keep = np.argmax(sums) + 1
    return labels == label_to_keep
