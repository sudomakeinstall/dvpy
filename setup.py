#!/usr/bin/env python3

from setuptools import setup, find_packages

setup(name='dvpy',
      version='0.1.0',
      description='Python Utilities',
      author='Davis Marc Vigneault',
      author_email='davis.vigneault@gmail.com',
      url='https://www.github.com/DVigneault/',
      packages=find_packages('src'),
      package_dir={'': 'src'},
      setup_requires=['pytest-runner'],
      tests_require=['pytest'],
      install_requires=['numpy', 'keras', 'matplotlib', 'pandas', 'nibabel', 'scikit-image', 'pypng'],
     )
