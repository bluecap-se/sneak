#!/usr/bin/python
# -*- coding: utf-8 -*-

import sneak

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
    name=sneak.__title__,
    description='Terminal snake in Python',
    long_description=readme,
    version=sneak.__version__,
    author='bluecap-se',
    author_email='hello@bluecap.se',
    url='https://github.com/bluecap-se/sneak',
    license='MIT',
    zip_safe=False,
    platforms='any',
    packages=['sneak'],
    install_requires=requirements,
    scripts=['bin/sneak'],
    keywords=['sneak', 'game', 'snake'],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Intended Audience :: End Users/Desktop',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: MacOS',
        'Operating System :: POSIX',
        'Programming Language :: Python :: 2 :: Only',
        'Topic :: Games/Entertainment :: Arcade',
    ]
)
