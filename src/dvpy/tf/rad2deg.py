import tensorflow as tf
import numpy as np

def rad2deg(x):
  return tf.multiply(x, tf.constant(180.0/np.pi))
