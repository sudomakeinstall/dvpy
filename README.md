# Install:

    $ pip install git+https://github.com/dvigneault/dvpy.git#egg=dvpy

The only dependency *not* installed by default is tensorflow, as we do not want to specify the GPU or CPU version.  These can be installed as follows:

    $ pipenv install tensorflow # CPU
    $ pipenv install tensorflow-gpu # GPU

# Run tests:

First, build your development environment (requires that Docker be installed and running):

    $ ./docker-build.sh

Spin up your container:

    $ ./docker-run.sh

And run your tests!

    $ pytest                                      # Run all the tests
    $ pytest ./test/test_find_duplicates.py       # Run a specific test
    $ pytest ./test/test_find_duplicates.py -v    # Be verbose
    $ pytest ./test/test_find_duplicates.py -v -s # Be super verbose

