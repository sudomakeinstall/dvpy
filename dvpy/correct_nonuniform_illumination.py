import numpy as np
from skimage.filters import gaussian

def correct_nonuniform_illumination(img, percentile = 25, sigma = 10):
  med = np.percentile(img, 25) 
  blr = img.copy()
  blr[blr < med] = med 
  return img / gaussian(blr, 10) 

