# System

# Third Party
import numpy as np

# Internal


def annotate_mu_sd(x):

    mu = np.mean(x)
    sd = np.std(x)

    return "$%.2f \pm %.2f$" % (mu, sd)
