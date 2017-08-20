import numpy as np

def annotate_mu_sd(x):

  mu = np.mean(x)
  sd = np.std( x)

  return '$%.2f \pm %.2f$'%(mu, sd)

