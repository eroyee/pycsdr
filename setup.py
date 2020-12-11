#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
from setuptools import setup, Extension

setup(
    name='pycsdr',
    version="0.18.0-dev",

    package_data={
        '': ['**.txt', '**.md', '**.py', '**.h', '**.hpp', '**.c', '**.cpp'],
    },

    ext_modules=[
        Extension(
            name='pycsdr',
            sources=[
                'src/socket_client.c',
            ],
            include_dirs=['src'],
        )
    ],
)
