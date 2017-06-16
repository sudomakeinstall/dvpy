import os

def determine_number_of_files(directory, pattern):
  """
  Determine how many files in a directory match a given pattern
  after substituting sequential integers starting from zero.

  Parameters
  ----------
  directory: str
    Base directory in which to look for files.
  pattern: str
    String pattern allowing a single digit substitution
    e.g., "img_%d.png"%(0) ==> "img_0.png"

  Returns
    N : int
    Number of files matching pattern sequentially, beginning with zero.
  -------
  """

  number_of_files = 0
  while (os.path.isfile(os.path.join(directory, pattern%(number_of_files)))):
    number_of_files += 1
  return number_of_files
