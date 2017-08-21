import keras.backend as K
import numpy as np

def number_of_model_weights(model):

  trainable_count = int(
    np.sum([K.count_params(p) for p in set(model.trainable_weights)]))

  non_trainable_count = int(
    np.sum([K.count_params(p) for p in set(model.non_trainable_weights)]))

  return (trainable_count, non_trainable_count)

