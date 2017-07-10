import tensorflow as tf
import dvpy.tf
import keras.backend as K

def wrapped_phase_difference_loss(y_true, y_pred):
  diff = dvpy.tf.wrapped_phase_difference(y_true, y_pred)
  return K.mean(K.square(diff), axis = -1)
