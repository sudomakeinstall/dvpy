import numpy as np

def fit_plane_to_points(points):

  assert(points.shape[1] == 3)

  augmented = np.concatenate([points, np.ones((points.shape[0], 1))], axis = 1)
  
  _, _, v = np.linalg.svd(augmented, full_matrices=False)
  
  coefs = v[3,:]
  coefs /= np.linalg.norm(coefs[0:3])

  return coefs

