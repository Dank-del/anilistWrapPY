#!/usr/bin/env python
import setuptools
from anilistWrapPY import __version__

with open("README.md", "r") as fh:
    long_description = fh.read()

with open("req.txt") as f:
    dependencies = [_.strip() for _ in f]


setuptools.setup(
    name="anilistWrapPY",
    version=__version__,
    description="Unofficial Anilist.co API Wrapper",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license="The Unlicense",
    author="Dank-del",
    author_email="sayan@pokurt.me",
    url="https://github.com/Dank-del/anilistWrapPY",
    packages=setuptools.find_packages(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Programming Language :: Python :: 3.8",
    ],
    install_requires=dependencies,
    python_requires=">=3.7",
)