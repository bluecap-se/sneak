#!/usr/bin/python

from setuptools import setup

import sneak


with open("README.md", "r") as f:
    readme = f.read()


setup(
    name=sneak.__title__,
    description="Terminal snake in Python",
    long_description=readme,
    long_description_content_type="text/markdown",
    version=sneak.__version__,
    author="bluecap-se",
    author_email="hello@bluecap.se",
    url="https://github.com/bluecap-se/sneak",
    license="MIT",
    zip_safe=False,
    platforms="any",
    packages=["sneak"],
    install_requires=["docopt==0.6.2"],
    scripts=["bin/sneak"],
    keywords=["sneak", "game", "snake"],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Intended Audience :: End Users/Desktop",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Operating System :: MacOS",
        "Operating System :: POSIX",
        "Programming Language :: Python :: 3 :: Only",
        "Topic :: Games/Entertainment :: Arcade",
    ],
)
