import png
import numpy as np

def save_png(image, file_name, bitdepth = 16, normalize = True):
    f = open(file_name, 'wb')
    w = png.Writer(image.shape[0], image.shape[1], greyscale=True, bitdepth=bitdepth)
    if normalize:
      image = image * (2**bitdepth - 1) / np.max(image)
    w.write(f, image)
    f.close()
