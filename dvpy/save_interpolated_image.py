import pylab as pl

def save_interpolated_image(array, fileName, colormap = 'gray'):
  pl.gca().set_axis_off()
  pl.gca().xaxis.set_major_locator(pl.NullLocator())
  pl.gca().yaxis.set_major_locator(pl.NullLocator())
  pl.imshow(array, cmap=colormap)
  pl.savefig(fileName, bbox_inches='tight', pad_inches=0)
  pl.close('all')
