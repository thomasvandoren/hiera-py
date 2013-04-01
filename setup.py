#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup

setup(
    author          ='Thomas Van Doren <thomas.vandoren@gmail.com>',
    name            ='hiera-py',
    version         ='0.0.1',
    packages        =['hiera'],
    description     ='Python interface for the hiera hierachical database.',
    long_description=open('README.md', 'r').read(),
    install_requires=[
        ],
    entry_points    ={
        'console_scripts': [
            ],
        },
    )
