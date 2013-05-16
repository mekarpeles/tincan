#!/usr/bin/env python
#-*- coding: utf-8 -*-

"""
    tincan
    ~~~~~~

    Setup
    `````
    $ pip install .
"""

from distutils.core import setup
import os

setup(
    name='tincan',
    version='0.1.692',
    url='http://github.com/mekarpeles/tincan',
    author='mek',
    author_email='michael.karpeles@gmail.com',
    packages=[
        'tincan',
        ],
    platforms='any',
    license='LICENSE',
    install_requires=[
        'waltz >= 0.1.68',
    ],
    description="Tincan is siri for dumb phones",
    long_description=open(os.path.join(
            os.path.dirname(__file__), 'README.md')
                          ).read(),
)
