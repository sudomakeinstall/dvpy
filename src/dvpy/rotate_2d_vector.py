import numpy as np

def rotate_2d_vector(vec, ang):
  rot = np.array([[np.cos(ang), -np.sin(ang)],
                  [np.sin(ang),  np.cos(ang)]])
  return np.dot(rot, vec)

