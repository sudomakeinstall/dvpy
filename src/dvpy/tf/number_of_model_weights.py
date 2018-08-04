# System
import collections as cl

# Third Party
import keras.backend as K
import numpy as np

# Internal


def number_of_model_weights(model):

    trainable_count = int(
        np.sum([K.count_params(p) for p in set(model.trainable_weights)])
    )

    non_trainable_count = int(
        np.sum([K.count_params(p) for p in set(model.non_trainable_weights)])
    )

    Weights = cl.namedtuple("Weights", ["trainable", "non_trainable"])
    return Weights(trainable=trainable_count, non_trainable=non_trainable_count)
