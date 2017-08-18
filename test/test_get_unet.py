import dvpy.tf

from keras.optimizers import Adam
from keras.models import Model
from keras.layers import Input

def test_get_unet():

  model_inputs = [Input((128, 128, 1))]

  _, _, output = dvpy.tf.get_unet(128, 5, 64, 0)(model_inputs[0])

  model_outputs = [output]

  model = Model(inputs = model_inputs,
                outputs = model_outputs)
  opt = Adam(lr = 1e-3)

  model.compile(optimizer = opt,
                loss = 'categorical_crossentropy',
               )
