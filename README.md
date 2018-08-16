# Install:

    $ pipenv install git+https://github.com/dvigneault/dvpy.git#egg=dvpy

The only dependency *not* installed by default is tensorflow, as we do not want to specify the GPU or CPU version.  These can be installed as follows:

    $ pipenv install tensorflow # CPU
    $ pipenv install tensorflow-gpu # GPU

# Run tests:

## Clone the repository:

    $ git clone git@github.com:DVigneault/dvpy.git ~/Developer/repositories/dvpy
    $ cd ~/Developer/repositories/dvpy

## Set up a development environment:
    $ pipenv shell

## Install a local copy, plus the dependencies:

    $ pipenv install -e ./
    $ pipenv install tensorflow # or tensorflow-gpu, as needed
    $ pipenv install pytest

## Run the tests!

    $ pytest                                      # Run all the tests
    $ pytest ./test/test_find_duplicates.py       # Run a specific test
    $ pytest ./test/test_find_duplicates.py -v    # Be verbose
    $ pytest ./test/test_find_duplicates.py -v -s # Be super verbose

