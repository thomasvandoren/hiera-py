#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup

setup(
    author ='Thomas Van Doren <thomas.vandoren@gmail.com>',
    name   ='hiera-py',
    version='0.0.1',
    packages=['hiera'],
    install_requires=[
        ],
    description     ='FIXME',
    entry_points    ={
        'console_scripts': [
            'hiera-py=hiera.client:HieraClient.cli',
            ],
        },
    )
