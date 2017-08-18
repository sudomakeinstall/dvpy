# Third Party
from keras.regularizers import l2
from keras.initializers import Orthogonal
from keras.layers.core import Activation
from keras.layers.normalization import BatchNormalization
from keras.layers import Input, \
                         Conv1D, Conv2D, Conv3D, \
                         MaxPooling1D, MaxPooling2D, MaxPooling3D, \
                         UpSampling1D, UpSampling2D, UpSampling3D, \
                         Reshape
from keras.layers.merge import concatenate, multiply
from keras.engine import Layer
from keras import backend as K
import numpy as np
import tensorflow as tf

# Internal
import dvpy as dv
import dvpy.tf

conv_dict = {1: Conv1D,
             2: Conv2D,
             3: Conv3D,
            }
max_pooling_dict = {1: MaxPooling1D,
                    2: MaxPooling2D,
                    3: MaxPooling3D,
                   }
up_sampling_dict = {1: UpSampling1D,
                    2: UpSampling2D,
                    3: UpSampling3D,
                   }


def conv_bn_relu_1x(nb_filter, kernel_size, subsample, dimension, weight_decay):
  sub = subsample*dimension
  Conv = conv_dict[dimension]
  def f(input_layer):
    conv_a = Conv(
               filters=nb_filter,
               kernel_size=kernel_size,
               strides=sub,
               padding='same',
               use_bias=False,
               kernel_initializer='orthogonal',
               kernel_regularizer = l2(weight_decay),
               bias_regularizer = l2(weight_decay))(input_layer)
    norm_a = BatchNormalization()(conv_a)
    act_a = Activation('relu')(norm_a)
    return act_a
  return f

def conv_bn_relu(nb_filter, kernel_size, subsample=(1,), dimension = 2, depth = 2, weight_decay = 1e-4):
    def f(input_layer):
        inputs = [input_layer]
        for i in range(depth):
            act = conv_bn_relu_1x(nb_filter, kernel_size, subsample, dimension, weight_decay)(inputs[i])
            inputs += [act]
        return inputs[depth]
    return f

def get_unet(dim, num_output_classes, conv_depth, stage, dimension = 2, weight_decay = 1e-4):
    if np.isscalar(dim):
      dim = (dim,)*dimension
    kernel_size=(3,)*dimension
    pool_size=(2,)*dimension

    MaxPooling = max_pooling_dict[dimension]
    UpSampling = up_sampling_dict[dimension]
    Conv = conv_dict[dimension]

    def f(input_layer):
        #
        level1 = conv_bn_relu(conv_depth, kernel_size, dimension = dimension)(input_layer)
        pool1 = MaxPooling(pool_size=pool_size)(level1)  # 128 x 128 x 64
        #
        level2 = conv_bn_relu(conv_depth, kernel_size, dimension = dimension)(pool1)
        pool2 = MaxPooling(pool_size=pool_size)(level2)  # 64 x 64 x 64
        #
        level3 = conv_bn_relu(conv_depth, kernel_size, dimension = dimension)(pool2)
        pool3 = MaxPooling(pool_size=pool_size)(level3)  # 32 x 32 x 64
        #
        level4 = conv_bn_relu(conv_depth, kernel_size, dimension = dimension)(pool3)
        pool4 = MaxPooling(pool_size=pool_size)(level4)  # 16 x 16 x 64
        #
        level5 = conv_bn_relu(conv_depth, kernel_size, dimension = dimension)(pool4)
        pool5 = MaxPooling(pool_size=pool_size)(level5)  # 8 x 8 x 64
        #
        level6 = conv_bn_relu(conv_depth, kernel_size, dimension = dimension)(pool5)
        up6 = concatenate([UpSampling(size=pool_size)(level6), level5]) # 16
        #
        level7 = conv_bn_relu(conv_depth, kernel_size, dimension = dimension)(up6)
        up7 = concatenate([UpSampling(size=pool_size)(level7), level4]) # 32
        #
        level8 = conv_bn_relu(conv_depth, kernel_size, dimension = dimension)(up7)
        up8 = concatenate([UpSampling(size=pool_size)(level8), level3]) # 64
        #
        level9 = conv_bn_relu(conv_depth, kernel_size, dimension = dimension)(up8)
        up9 = concatenate([UpSampling(size=pool_size)(level9), level2]) # 128
        #
        level10 = conv_bn_relu(conv_depth, kernel_size, dimension = dimension)(up9)
        up10 = concatenate([UpSampling(size=pool_size)(level10), level1]) # 256
        #
        final_feature = conv_bn_relu(conv_depth, kernel_size, dimension = dimension)(up10)
        conv11 = Conv(
                        num_output_classes,
                        kernel_size,
                        padding='same',
                        activation='linear',
                        kernel_initializer='orthogonal',
                        kernel_regularizer = l2(weight_decay),
                        bias_regularizer = l2(weight_decay),
                       )(final_feature)
        conv12 = Reshape((np.product(dim), num_output_classes))(conv11)
        conv13 = Activation(activation='softmax')(conv12)

        # segmentation loss
        seg_pred = Reshape(dim + (num_output_classes,), name = 'img_sg%d'%(stage))(conv13)
        return pool5, final_feature, seg_pred
    return f

