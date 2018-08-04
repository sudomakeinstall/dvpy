# System

# Third Party
import numpy as np

# Internal


def annotate_iqr(x):
    x25 = np.percentile(x, 25)
    x50 = np.percentile(x, 50)
    x75 = np.percentile(x, 75)

    return "$%.2f [%.2f, %.2f]$" % (x50, x25, x50)
