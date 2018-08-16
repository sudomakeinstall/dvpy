# System

# Third Party
from keras.regularizers import l2
from keras.initializers import Orthogonal
from keras.layers.core import Activation
from keras.layers.normalization import BatchNormalization
from keras.layers import (
    Input,
    Conv1D,
    Conv2D,
    Conv3D,
    MaxPooling1D,
    MaxPooling2D,
    MaxPooling3D,
    UpSampling1D,
    UpSampling2D,
    UpSampling3D,
    Reshape,
    ZeroPadding1D,
    ZeroPadding2D,
    ZeroPadding3D,
)
from keras.layers.merge import concatenate, multiply
from keras.engine import Layer
from keras import backend as K
import numpy as np
import tensorflow as tf

# Internal

conv_dict = {1: Conv1D, 2: Conv2D, 3: Conv3D}
max_pooling_dict = {1: MaxPooling1D, 2: MaxPooling2D, 3: MaxPooling3D}
up_sampling_dict = {1: UpSampling1D, 2: UpSampling2D, 3: UpSampling3D}
zero_sampling_dict = {1: ZeroPadding1D, 2: ZeroPadding2D, 3: ZeroPadding3D}


def conv_bn_relu_1x(nb_filter, kernel_size, subsample, dimension, weight_decay):
    sub = subsample * dimension
    Conv = conv_dict[dimension]

    def f(input_layer):
        conv_a = Conv(
            filters=nb_filter,
            kernel_size=kernel_size,
            strides=sub,
            padding="same",
            use_bias=False,
            kernel_initializer="orthogonal",
            kernel_regularizer=l2(weight_decay),
            bias_regularizer=l2(weight_decay),
        )(input_layer)
        norm_a = BatchNormalization()(conv_a)
        act_a = Activation("relu")(norm_a)
        return act_a

    return f


def conv_bn_relu(
    nb_filter, kernel_size, subsample=(1,), dimension=2, depth=2, weight_decay=1e-4
):
    def f(input_layer):
        inputs = [input_layer]
        for i in range(depth):
            act = conv_bn_relu_1x(
                nb_filter, kernel_size, subsample, dimension, weight_decay
            )(inputs[i])
            inputs += [act]
        return inputs[depth]

    return f


def get_padding(shape, dimension):
    x_crop = 1 if shape[1] % 2 == 1 else 0
    if dimension == 1:
        return (0, x_crop)
    y_crop = 1 if shape[2] % 2 == 1 else 0
    if dimension == 2:
        return ((0, x_crop), (0, y_crop))
    z_crop = 1 if shape[3] % 2 == 1 else 0
    return ((0, x_crop), (0, y_crop), (0, z_crop))


def get_unet(
    dim,
    num_output_classes,
    conv_depth,
    layer_name=None,
    dimension=2,
    weight_decay=1e-4,
    unet_depth=3,
):

    if np.isscalar(dim):
        dim = (dim,) * dimension
    else:
        assert len(dim) == dimension

    if np.isscalar(conv_depth):
        conv_depth = [conv_depth] * (2 * unet_depth + 1)
    else:
        assert len(conv_depth) == 2 * unet_depth + 1

    kernel_size = (3,) * dimension
    pool_size = (2,) * dimension

    MaxPooling = max_pooling_dict[dimension]
    UpSampling = up_sampling_dict[dimension]
    ZeroPadding = zero_sampling_dict[dimension]
    Conv = conv_dict[dimension]

    def f(input_layer):
        #
        levels = []
        ds = []
        us = []

        for i in range(unet_depth):
            if 0 == i:
                levels += [
                    conv_bn_relu(conv_depth[i], kernel_size, dimension=dimension)(
                        input_layer
                    )
                ]
            else:
                levels += [
                    conv_bn_relu(conv_depth[i], kernel_size, dimension=dimension)(
                        ds[-1]
                    )
                ]
            ds += [MaxPooling(pool_size=pool_size)(levels[-1])]

        for i in range(unet_depth):
            if 0 == i:
                levels += [
                    conv_bn_relu(
                        conv_depth[i + unet_depth], kernel_size, dimension=dimension
                    )(ds[-1])
                ]
            else:
                levels += [
                    conv_bn_relu(
                        conv_depth[i + unet_depth], kernel_size, dimension=dimension
                    )(us[-1])
                ]
            us += [
                concatenate(
                    [UpSampling(size=pool_size)(levels[-1]), levels[unet_depth - i - 1]]
                )
            ]
        #            padding = get_padding(K.int_shape(levels[unet_depth - i - 1]), dimension)
        #            us += [
        #                concatenate(
        #                    [
        #                        ZeroPadding(padding)(UpSampling(size=pool_size)(levels[-1])),
        #                        levels[unet_depth - i - 1],
        #                    ]
        #                )
        #            ]

        final_feature = conv_bn_relu(
            conv_depth[unet_depth * 2], kernel_size, dimension=dimension
        )(us[-1])
        conv11 = Conv(
            num_output_classes,
            kernel_size,
            padding="same",
            activation="linear",
            kernel_initializer="orthogonal",
            kernel_regularizer=l2(weight_decay),
            bias_regularizer=l2(weight_decay),
        )(final_feature)
        # print(conv11.shape)
        conv12 = Reshape((np.product(dim), num_output_classes))(conv11)
        conv13 = Activation(activation="softmax")(conv12)

        # segmentation loss
        seg_pred = Reshape(dim + (num_output_classes,), name=layer_name)(conv13)
        return ds[-1], final_feature, seg_pred

    return f
