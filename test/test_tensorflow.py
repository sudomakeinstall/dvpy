import tensorflow as tf
import numpy as np
import dvpy as dv
import dvpy.tf


def test_tf_conversions():
    deg = tf.convert_to_tensor([[x * 90.0 - 360.0 for x in range(9)]])
    rad = tf.convert_to_tensor([[x * np.pi / 2.0 - 2.0 * np.pi for x in range(9)]])

    with tf.Session() as s:
        assert np.all(s.run(tf.equal(deg, dvpy.tf.rad2deg(rad))))
        assert np.all(s.run(tf.equal(rad, dvpy.tf.deg2rad(deg))))


def test_tf_phase():
    a = np.expand_dims(np.linspace(-np.pi, np.pi, 101, "float32"), -1).transpose()
    b = -a
    c = dv.wrap_phase(b - a)

    a_tf = tf.convert_to_tensor(a, "float32")
    b_tf = tf.convert_to_tensor(b, "float32")
    c_tf = dvpy.tf.wrapped_phase_difference(a_tf, b_tf)

    with tf.Session() as s:
        c_tf_eval = s.run(c_tf)
        assert np.allclose(c_tf_eval, c)
