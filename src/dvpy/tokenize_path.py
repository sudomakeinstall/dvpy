import pathlib as pl

def tokenize_path(path):
  return pl.PurePath(path).parts
