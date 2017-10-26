# System

# Third Party
import numpy as np

# Internal

def rotation_matrix_from_angle(ang):
  return np.array([[np.cos(ang), -np.sin(ang)],
                   [np.sin(ang),  np.cos(ang)]])

