
import tensorflow as tf

def run_and_print(x):
  with tf.Session() as s:
    print(s.run(x))
