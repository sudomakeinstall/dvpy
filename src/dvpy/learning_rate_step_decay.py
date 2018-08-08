import numpy as np


def learning_rate_step_decay(epoch, lr, step=24, initial_power=-3):
    """
    The learning rate begins at 10^initial_power,
    and decreases by a factor of 10 every `step` epochs.
    """
    num = epoch // step
    lrate = 10 ** (initial_power - num)
    print("Learning rate for epoch {} is {}.".format(epoch + 1, 1.0 * lrate))
    return np.float(lrate)
