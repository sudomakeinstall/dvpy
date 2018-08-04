# System

# Third Party
import tensorflow as tf

# Internal
import dvpy.tf


def wrapped_phase_difference(y_true, y_pred):
    """
  Return the wrapped difference between `y_true` and `y_pred`.
  Note that `y_true` and `y_pred` are expected to be *principal* phase angles
  in radians, i.e., [-pi, pi).
  """

    diff = y_pred - y_true
    diff -= tf.multiply(
        tf.cast(tf.greater_equal(diff, dvpy.tf.pi), "float32"), 2.0 * dvpy.tf.pi
    )
    diff += tf.multiply(
        tf.cast(tf.less(diff, -dvpy.tf.pi), "float32"), 2.0 * dvpy.tf.pi
    )
    return diff
