# System
import pathlib as pl

# Third Party

# Internal


def tokenize_path(path):
    return pl.PurePath(path).parts
