#!/usr/bin/env python

import os
import re

from setuptools import setup, find_packages

setup(
    name="shipwreck",
    version="0.0.1",
    description="An experiment with using blob storage as my recordings storage!",
    long_description=open("README.md", "r").read(),
    long_description_content_type="text/markdown",
    license="MIT License",
    author="semick-dev",
    author_email="sbeddall@live.com",
    url="https://github.com/semick-dev/shipwreck",
    classifiers=[
        "Development Status :: 3 - Alpha",
    ],
    packages=find_packages(exclude=["tests"]),
    python_requires=">=3.6",
    install_requires=["azure-storage-blob>=12.10.0"],
    entry_points={"console_scripts": ["ship = ship:main"]},
)
