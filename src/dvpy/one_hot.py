import numpy as np
import keras.utils.np_utils as k

def one_hot(image, num_classes):
  """
  One-hot encode an image
  """
  return np.reshape(k.to_categorical(image.flatten(), num_classes = num_classes),
                    image.shape + (num_classes,))
