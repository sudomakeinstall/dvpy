# Standard

# Third Party
import keras.backend as K

# Internal
import dvpy.tf


def wrapped_phase_difference_loss(y_true, y_pred):
    diff = dvpy.tf.wrapped_phase_difference(y_true, y_pred)
    return K.mean(K.square(diff), axis=-1)
