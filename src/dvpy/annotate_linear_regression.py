
from scipy.stats import linregress
import dvpy as dv

def annotate_linear_regression(x, y):
  reg = linregress(x, y)
  m = reg[0]
  b = reg[1]
  r = reg[2]
  p = reg[3]
  p = dv.format_p_value(p)
  
  return '$y = %.2f x + %.2f$\n$R = %.2f$ ($%s$)'%(m, b, r, p)

