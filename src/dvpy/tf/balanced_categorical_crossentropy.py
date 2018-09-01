from keras import backend as K
import tensorflow as tf

import dvpy.tf


def balanced_categorical_crossentropy(y_true, y_pred):
    """
    Calculates a weighted version of categorical_crossentropy, where the
    individual pixel losses are weighted according to 1-normalized_frequency.
    This has the effect of balancing classes.  Importantly, the weights are calculated
    batchwise.

    Inspired by:
    https://gist.github.com/wassname/ce364fddfc8a025bfab4348cf5de852d
    """

    weights = dvpy.tf.normalized_class_frequencies(y_true)
    y_pred /= K.sum(y_pred, axis=-1, keepdims=True)
    y_pred = K.clip(y_pred, K.epsilon(), 1 - K.epsilon())
    loss = y_true * K.log(y_pred) * weights
    return -K.sum(loss, -1)
