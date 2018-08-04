import dvpy.tf

from keras.optimizers import Adam
from keras.models import Model
from keras.layers import Input


def test_get_unet():

    for d in [2, 3]:
        shape = (128,) * d + (1,)

        model_inputs = [Input(shape)]

        _, _, output = dvpy.tf.get_unet(128, 5, 64, 0, dimension=d)(model_inputs[0])

        model_outputs = [output]

        model = Model(inputs=model_inputs, outputs=model_outputs)
        opt = Adam(lr=1e-3)

        model.compile(optimizer=opt, loss="categorical_crossentropy")

        print(dvpy.tf.number_of_model_weights(model))
