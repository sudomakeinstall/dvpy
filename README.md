# Install:

    $ pip install git+https://github.com/dvigneault/dvpy.git

# Update:

    $ pip install git+https://github.com/dvigneault/dvpy.git --upgrade

# Run tests:

## First, set up a development environment.

    $ sudo apt-get install python3-venv python3-matplotlib
    $ python3 -m venv .venv
    $ . ./.venv/bin/activate
    $ pip install --upgrade pip setuptools

## Second, install `dvpy` in edit (i.e., development) mode.

    $ pip install -e ./

## Third, install the third party packages.

    $ pip install pytest nibabel numpy pandas pypng scikit-image scipy
    $ pip install tensorflow-gpu pyyaml h5py keras

## Run the tests!

    $ python -m pytest       # Just run tests
    $ python -m pytest -v    # Be verbose
    $ python -m pytest -v -s # Be super verbose

