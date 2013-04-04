#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup

setup(
    name            ='hiera-py',
    version         ='0.0.1',
    description     ='Python interface for the hiera hierachical database.',
    long_description=open('README.rst', 'r').read(),
    author          ='Thomas Van Doren',
    author_email    ='thomas@thomasvandoren.com',
    maintainer      ='Thomas Van Doren',
    maintainer_email='thomas@thomasvandoren.com',
    url             ='http://thomasvandoren.github.com/hiera-py',
    keywords        =['hiera'],
    license         ='BSD',
    packages        =['hiera'],
    classifiers     =[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        ],
    )
