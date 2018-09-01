import numpy as np


def jaccard_index(y_true, y_pred, label, epsilon=1e-5):
    """
    Calculate the Jaccard index (i.e., intersection-over-union) between
    a ground truth (y_true) and predicted (y_pred) segmentation for
    a given segmentation label (label).
    https://en.wikipedia.org/wiki/Jaccard_index
    """

    # Binarize y_true and y_pred, such that the label becomes
    # foreground (1) and all other labels become background (0).
    y_true_bin = np.asarray(y_true == label, dtype="bool")
    y_pred_bin = np.asarray(y_pred == label, dtype="bool")

    # Calculate the intersection (logical AND operation) and union
    # (logical OR operation), and the ratio of the two.
    # A small value (epsilon) is added to the denominator to prevent
    # undefined results if neither segmentation contains the
    # requested label.
    Intersection = np.sum(np.logical_and(y_true_bin, y_pred_bin))
    Union = np.sum(np.logical_or(y_true_bin, y_pred_bin))
    return Intersection / (Union + epsilon)


def dice_coefficient(y_true, y_pred, label, epsilon=1e-5):
    """
    Calculate the Dice coefficient between a ground truth (y_true)
    and predicted (y_pred) segmentation for a given segmentation
    label (label).
    https://en.wikipedia.org/wiki/S%C3%B8rensen%E2%80%93Dice_coefficient
    """

    # Binarize y_true and y_pred, such that the label becomes
    # foreground (1) and all other labels become background (0).
    y_true_bin = np.asarray(y_true == label, dtype="bool")
    y_pred_bin = np.asarray(y_pred == label, dtype="bool")

    # Calculate the intersection (logical AND operation), sum,
    # and Dice coefficient.  A small value (epsilon) is added
    # to the denominator to prevent undefined results if neither
    # segmentation contains the requested label.
    Intersection = np.sum(np.logical_and(y_true_bin, y_pred_bin))
    Sum = np.sum(y_true_bin) + np.sum(y_pred_bin)
    return 2 * Intersection / (Sum + epsilon)


def jaccard_to_dice(j):
    if (j < 0.0) or (j > 1.0):
        raise ValueError("Jaccard index {} is out of the range [0.0, 1.0]".format(j))
    return 2 * j / (1 + j)


def dice_to_jaccard(d):
    if (d < 0.0) or (d > 1.0):
        raise ValueError("Dice coefficient {} is out of the range [0.0, 1.0]".format(d))
    return d / (2 - d)
