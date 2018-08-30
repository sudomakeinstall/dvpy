# System

# Third Party
import numpy as np
import keras.utils.np_utils as k

# Internal


def one_hot(array, num_classes):
    """
    One-hot encode an array.

    :param array: An input segmentation.
    :type array: nd-array with unsigned integers.

    :param num_classes: The length of the output vector.
    :type num_classes: unsigned int

    :returns: The segmentation, with each pixel coded as a one-hot array.
    :rtype: array-like, of shape array.shape + (num_classes,)
    """
    return np.reshape(
        k.to_categorical(array.flatten(), num_classes=num_classes),
        array.shape + (num_classes,),
    )
