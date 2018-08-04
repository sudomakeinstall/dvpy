# System
import os

# Third Party

# Internal


def determine_number_of_files(directory, pattern):
    """
  Determine how many files in a directory match a given pattern
  after substituting sequential integers starting from zero.

  :param directory: Base directory in which to look for files.
  :type directory: str

  :param pattern: String pattern allowing a single digit substitution
    e.g., "img_%d.png"%(0) ==> "img_0.png"
  :type pattern: str

  :returns: Number of files matching pattern sequentially, beginning with zero.
  :rtype: int
  """

    number_of_files = 0
    while os.path.isfile(os.path.join(directory, pattern % (number_of_files))):
        number_of_files += 1
    return number_of_files
