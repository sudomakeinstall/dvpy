# System

# Third Party
import png
import numpy as np

# Internal


def save_png(image, file_name, bitdepth=16, normalize=True):
    f = open(file_name, "wb")
    w = png.Writer(image.shape[1], image.shape[0], greyscale=True, bitdepth=bitdepth)
    if normalize:
        image = image * (2 ** bitdepth - 1) / np.max(image)
    if bitdepth == 16:
        image = image.astype(np.uint16)
    elif bitdepth == 8:
        image = image.astype(np.uint8)
    else:
        print("WARNING: Bitdepth %d not recognized." % (bitdepth))
    w.write(f, image)
    f.close()
