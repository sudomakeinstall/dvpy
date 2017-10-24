# System

# Third Party
import numpy as np
from keras import backend as K

# Internal
import dvpy as dv
from . import IteratorBase

class NumpyArrayIterator(IteratorBase):

    def __init__(self,
                 X,
                 y,
                 image_data_generator,
                 batch_size=32,
                 shuffle=False,
                 seed=None,
                 dim_ordering='default',
                 save_to_dir=None,
                 save_prefix='',
                 save_format='jpeg',
                 input_adapter = None,
                 output_adapter = None,
                 shape = None,
                 input_channels = None,
                 output_channels = None,
                 predict = False,
                 view_predict = False,
                 output_views = None,
                 view_opt = None,
                 get_view_type = None,
                 hourglass_depth = None,
                ):

        if len(X) != len(y):

            raise Exception('X (images tensor) and y (labels) '
                            'should have the same length. '
                            'Found: X.shape = %s, y.shape = %s' % (np.asarray(X).shape, np.asarray(y).shape))
        if dim_ordering == 'default':
            dim_ordering = K.image_dim_ordering()
        self.X = X
        self.y = y
        self.image_data_generator = image_data_generator
        self.dim_ordering = dim_ordering
        self.save_to_dir = save_to_dir
        self.save_prefix = save_prefix
        self.save_format = save_format
        self.input_adapter = input_adapter
        self.output_adapter = output_adapter
        self.shape = shape
        self.input_channels = input_channels
        self.output_channels = output_channels
        self.predict = predict
        self.view_predict = view_predict
        self.output_views = output_views
        self.view_opt = view_opt
        self.get_view_type = get_view_type
        self.hourglass_depth = hourglass_depth
        super(NumpyArrayIterator, self).__init__(X.shape[0], batch_size, shuffle, seed)



    def next(self):
        # for python 2.x.
        # Keeps under lock only the mechanism which advances
        # the indexing of each batch
        # see http://anandology.com/blog/using-iterators-and-generators/
        with self.lock:
            index_array, current_index, current_batch_size = next(self.index_generator)
        # The transformation of images is not under thread lock so it can be done in parallel
            
        ##
        ## Allocate Memory
        ##
        
        # Input Image in range 0 to 1
        batch_x = np.zeros(tuple([current_batch_size])+self.shape+tuple([self.input_channels]))
        
        # Ground Truth Segmentation
        batch_y = np.zeros(tuple([current_batch_size])+self.shape+tuple([self.output_channels]))

        ##
        ## Deal with Actual Data
        ##

        # index_array is a randomly shuffled list of cases for this batch
        for i, j in enumerate(index_array):

            # Retrieve the path to the input image...
            x = self.X[j]
            # ...and convert the path to a raw (unnormalized) image.
            if self.input_adapter is not None:
                x = self.input_adapter(x)

            # Retrieve the path to the segmentation...
            label = self.y[j]
            if self.output_adapter is not None:
                # ...and convert the path to a one-hot encoded image.
                label = self.output_adapter(label)

#            # If *training*, we want to augment the data.
#            # If *testing*, we do not.
#            if not self.predict:
#                x, label, aug_ang = self.image_data_generator.random_transform(x.astype('float32'), label.astype('float32'))
#            else:
#                aug_ang = 0.0

            # Normalize the *individual* image from zero to one.
            batch_x[i] = dv.normalize_image(x)
            batch_y[i] = label

        ##
        ## Return
        ##

        inputs = {'input_1' : batch_x,}
        outputs = {'img_sg0' : batch_y,}

        return (inputs, outputs,)

