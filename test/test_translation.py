import numpy as np
from keras import backend as K
from keras.optimizers import Adam
from keras.models import Model
from keras.layers import Input
from keras.layers import (
    Conv3D,
    MaxPooling3D,
    Input,
    UpSampling3D,
    Reshape,
    ZeroPadding3D,
    Cropping3D,
)
from keras.layers.merge import concatenate
from keras import backend as K
from keras.models import Model
from keras.regularizers import l2
from keras.initializers import Orthogonal
from keras.layers.core import Activation
from keras.layers.normalization import BatchNormalization


def get_padding(shape):
    b_crop = 1 if shape[1] % 2 == 1 else 0
    c_crop = 1 if shape[2] % 2 == 1 else 0
    d_crop = 1 if shape[3] % 2 == 1 else 0
    return ((0, b_crop), (0, c_crop), (0, d_crop))


def get_padding(shape):
    b_crop = 1 if shape[1] % 2 == 1 else 0
    c_crop = 1 if shape[2] % 2 == 1 else 0
    d_crop = 1 if shape[3] % 2 == 1 else 0
    return ((0, b_crop), (0, c_crop), (0, d_crop))


def conv_bn_relu_1x(nb_filter, kernel_size, input_layer):

    Conv = Conv3D

    conv_a = Conv(
        filters=nb_filter,
        kernel_size=kernel_size,
        padding="same",
        use_bias=False,
        kernel_initializer="orthogonal",
    )(input_layer)
    norm_a = BatchNormalization()(conv_a)
    act_a = Activation("relu")(norm_a)
    return act_a


image = Input((30, 30, 30, 1))
conv1 = conv_bn_relu_1x(16, (3, 3, 3), image)

pool1 = MaxPooling3D(
    pool_size=(2, 2, 2), strides=None, padding="valid", data_format=None
)(conv1)
conv2 = conv_bn_relu_1x(32, (3, 3, 3), pool1)
pool2 = MaxPooling3D(
    pool_size=(2, 2, 2), strides=None, padding="valid", data_format=None
)(conv2)
conv3 = conv_bn_relu_1x(32, (3, 3, 3), pool2)
up1 = UpSampling3D(size=(2, 2, 2))(conv3)

padding = get_padding(K.int_shape(conv2))
up1_ = ZeroPadding3D((padding))(up1)
concat1 = concatenate([up1_, conv2])
# print(concat1.shape)
conv4 = conv_bn_relu_1x(32, (3, 3, 3), concat1)
up2 = UpSampling3D(size=(2, 2, 2))(conv4)
# print(up2.shape)
padding = get_padding(K.int_shape(conv1))
up2_ = ZeroPadding3D((padding))(up2)
concat2 = concatenate([up2_, conv1])
con5 = conv_bn_relu_1x(32, (3, 3, 3), concat2)
output = conv_bn_relu_1x(1, (3, 3, 3), con5)


model = Model(inputs=image, outputs=output)
model.compile(loss="mean_squared_error", optimizer="adam")


# In[17]:
input = np.zeros((1, 30, 30, 30, 1))
input[0, 10, 10:-10, 10:-10] = 1
temp_input = input.copy()
input = K.variable(input)

model.fit(input, input, batch_size=None, steps_per_epoch=1, epochs=2000, verbose=1)


y = model.predict(input, steps=1)
y = np.round(y)
print(np.sum(y))
assert (y == temp_input).all()
