import tensorflow as tf


def normalized_class_frequencies(x):
    """
    x should be a one-hot tensor
    """
    class_frequencies = tf.reduce_sum(x, list(range(x.shape.ndims - 1)))
    denominator = tf.cast(tf.reduce_prod(tf.shape(x)[:-1]), x.dtype)
    return class_frequencies / denominator
