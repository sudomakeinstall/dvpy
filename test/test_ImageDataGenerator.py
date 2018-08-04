import dvpy as dv
import numpy as np


def test_ImageDataGenerator():

    gen = dv.tf.ImageDataGenerator(3)
    gen.random_transform(np.ones((25, 25, 25, 3)), np.ones((25, 25, 25, 3)))
