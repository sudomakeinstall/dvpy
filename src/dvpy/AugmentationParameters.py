
import numpy as np


def expand_if_scalar(maybe_scalar, dimension):
    if np.isscalar(maybe_scalar):
        return (maybe_scalar,) * dimension
    elif len(maybe_scalar) == dimension:
        return maybe_scalar
    else:
        raise Exception(
            "maybe_scalar should be either a float, or an array-like length dimension"
        )


class AugmentationParameters:
    __slots__ = [
        "image_dimension",
        "translation_range",
        "rotation_range",
        "scale_range",
        "flip",
        "fill_mode",
        "cval",
        "img_spatial_indices",
        "img_channel_index",
    ]

    def __init__(
        self,
        image_dimension,
        translation_range=0.0,
        rotation_range=0.0,
        scale_range=1.0,
        flip=False,
        fill_mode="constant",
        cval=0.0,
    ):

        self.image_dimension = image_dimension

        self.translation_range = expand_if_scalar(
            translation_range, self.image_dimension
        )
        if np.isscalar(scale_range):
            self.scale_range = scale_range
        else:
            raise Exception(
                "scale_range must be a float (only rigid scaling is supported)"
            )
        self.flip = expand_if_scalar(flip, self.image_dimension)
        self.fill_mode = fill_mode
        self.cval = cval

        self.img_spatial_indices = np.array(range(0, image_dimension))
        self.img_channel_index = image_dimension

        ##
        ## Rotation should be handled separately for each image dimension
        ##

        if self.image_dimension == 2:
            if not np.isscalar(rotation_range):
                raise Exception(
                    "rotation_range should be a float when image_dimension is 2"
                )
            self.rotation_range = rotation_range
        elif self.image_dimension == 3:
            if np.isscalar(rotation_range):
                self.rotation_range = (rotation_range,) * self.image_dimension
            elif len(rotation_range) == self.image_dimension:
                self.rotation_range = rotation_range
            else:
                raise Exception(
                    "rotation_range should be either a float, or an array-like length image_dimension when image_dimension is 3"
                )
        else:
            raise Exception("Only image dimensions 2 and 3 are supported")

    def __str__(self):

        return "\n".join(
            ["{} : {}".format(attr, getattr(self, attr)) for attr in self.__slots__]
        )
