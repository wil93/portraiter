#!/usr/bin/env python2
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name="portraiter",
    version="0.1",
    author="William Di Luigi",
    author_email="williamdiluigi@gmail.com",
    url="https://github.com/wil93/portraiter",
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "portraiter=portraiter.portraiter:main",
        ]
    },
    license="General Public License v3",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Natural Language :: English",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python :: 2",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)"
    ]
)
