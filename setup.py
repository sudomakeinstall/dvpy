#!/usr/bin/env python3

from setuptools import setup

setup(name='dvpy',
      version='0.1',
      description='Python Utilities',
      author='Davis Marc Vigneault',
      author_email='davis.vigneault@gmail.com',
      url='https://www.github.com/DVigneault/',
      packages=['dvpy'],
      setup_requires=['pytest-runner'],
      tests_require=['pytest'],
     )
