import tensorflow as tf
import numpy as np

def deg2rad(x):
  return tf.multiply(x, tf.constant(np.pi/180.0))
