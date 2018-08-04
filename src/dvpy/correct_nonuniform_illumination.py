# System

# Third Party
import numpy as np
from skimage.filters import gaussian

# Internal


def correct_nonuniform_illumination(img, percentile=25, sigma=10, epsilon=10e-6):
    """
  Attempt to correct nonuniform background illumination in an image.

  :param img: Image to be background corrected.
  :type img: real-valued array-like

  :param percentile: All pixels below this percentile are considered background.
  :type percentile: number

  :param sigma: Radius of Gaussian blur.
  :type sigma: number

  :returns: Background-corrected image.
  :rtype: real-valued array-like

  """
    med = np.percentile(img, percentile)
    blr = img.copy()
    blr[blr < med] = med
    return img / (gaussian(blr, sigma) + epsilon)
