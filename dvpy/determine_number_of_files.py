import os

def determine_number_of_files(directory, extension):
  number_of_files = 0
  while (os.path.isfile(os.path.join(directory, '%d.%s'%(number_of_files, extension)))):
    number_of_files += 1
  return number_of_files
