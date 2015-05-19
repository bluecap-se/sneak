#!/usr/bin/python
# -*- coding: utf-8 -*-

import snake

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


with open('README.md') as f:
    readme = f.read()
with open('HISTORY.md') as f:
    history = f.read()
with open('requirements.txt') as f:
    requirements = f.read().splitlines()


setup(
    name=snake.__title__,
    description='Terminal Snake',
    long_description=readme,
    version=snake.__version__,
    author='bluecap-se',
    author_email='hello@bluecap.se',
    url='https://github.com/bluecap-se/snake',
    license='MIT',
    zip_safe=False,
    platforms='any',
    packages=['snake'],
    install_requires=requirements,
    scripts=['bin/snake'],
    keywords=['snake', 'game'],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: MacOS',
        'Operating System :: POSIX',
        'Programming Language :: Python :: 2 :: Only',
    ]
)
