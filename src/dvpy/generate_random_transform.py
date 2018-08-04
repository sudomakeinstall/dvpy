import dvpy as dv
import numpy as np


def generate_random_transform(params, shape):

    ##
    ## Translation
    ##

    translation = np.eye(params.image_dimension + 1)

    for t, ax in zip(params.translation_range, params.img_spatial_indices):
        translation[ax, params.image_dimension] = np.random.uniform(-t, t) * shape[ax]

    ##
    ## Rotation
    ##

    rotation = np.eye(params.image_dimension + 1)

    if params.image_dimension == 2:

        theta = (
            np.pi
            / 180.0
            * np.random.uniform(-params.rotation_range, params.rotation_range)
        )

        rotation[:2, :2] = dv.rotation_matrix_from_angle(theta)
    elif params.image_dimension == 3:
        x = dv.rotation_matrix_from_angle(
            np.pi
            / 180.0
            * np.random.uniform(-params.rotation_range[0], params.rotation_range[0]),
            matrix_type="roll",
        )
        y = dv.rotation_matrix_from_angle(
            np.pi
            / 180.0
            * np.random.uniform(-params.rotation_range[1], params.rotation_range[1]),
            matrix_type="pitch",
        )
        z = dv.rotation_matrix_from_angle(
            np.pi
            / 180.0
            * np.random.uniform(-params.rotation_range[2], params.rotation_range[2]),
            matrix_type="yaw",
        )
        rotation[:3, :3] = np.dot(z, np.dot(y, x))
    else:
        raise Exception("image_dimension must be either 2 or 3.")

    ##
    ## Scale
    ##

    scale = np.eye(params.image_dimension + 1)
    scale_factor = np.random.uniform(1 - params.scale_range, 1 + params.scale_range)
    for ax in params.img_spatial_indices:
        scale[ax, ax] = scale_factor

    ##
    ## Flip
    ##

    flip = np.eye(params.image_dimension + 1)

    for f, ax in zip(params.flip, params.img_spatial_indices):
        if f and (np.random.random() < 0.5):
            flip[ax, ax] *= -1

    ##
    ## Compose
    ##

    return np.dot(scale, np.dot(rotation, translation))
