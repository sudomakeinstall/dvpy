# System

# Third Party
import tensorflow as tf

# Internal


def run_and_print(x):
    with tf.Session() as s:
        print(s.run(x))
