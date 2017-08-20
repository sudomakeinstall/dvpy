import dvpy as dv
from scipy.stats import ttest_rel
import numpy as np

def annotate_bland_altman(x, y, x_label = None, y_label = None):
  p = ttest_rel(x, y)[1]
  p = dv.format_p_value(p)

  x_mu = np.mean(x)
  x_sd = np.std( x)
  y_mu = np.mean(y)
  y_sd = np.std( y)

  if x_label is not None and y_label is not None:
    x_label = ' (%s) '%(x_label)
    y_label = ' (%s) '%(y_label)
  else:
    x_label = ''
    y_label = ''

  annot  = '%s%s'%(dv.annotate_mu_sd(x), x_label)
  annot += ' vs '
  annot += '%s%s'%(dv.annotate_mu_sd(y), y_label)
  annot += '\n($%s$)'%(p)

  return annot
 
