#!/usr/bin/env python3

import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="listip",
    version="0.0.2",
    author="p7e4",
    author_email="p7e4@qq.com",
    description="Expand ip segment/cidr, for scanners",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/p7e4/listip",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
)

