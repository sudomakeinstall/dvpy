import numpy as np
from keras.activations import softmax
from keras.objectives import categorical_crossentropy
from keras import backend as K
import dvpy as dv
import tensorflow as tf


def test_balanced_categorical_crossentropy():

    samples = (2,)
    img_dim = (3, 3)
    num_classes = 5

    y_true_n = np.random.randint(0, num_classes, samples + img_dim)
    y_true_n = dv.one_hot(y_true_n, num_classes)

    y_true = K.variable(y_true_n)

    y_pred_n = np.random.random(samples + img_dim + (num_classes,)).astype(K.floatx())
    y_pred = K.variable(y_pred_n)
    y_pred = softmax(y_pred)

    loss = dv.tf.balanced_categorical_crossentropy(y_true, y_pred).eval(
        session=K.get_session()
    )
    print(loss)
