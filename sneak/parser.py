# -*- coding: utf-8 -*-

"""
Sneak: A terminal snake game

Usage: run.py [options]

Options:
  -h, --help            show this help message and exit
  -s SIZE, --size=SIZE  Game size (s | m | l)

"""
from docopt import docopt


def init():

    arguments = docopt(__doc__, version='TODO', options_first=True)

    options = {
        'size': arguments.get('--size', False) or 'm',
    }

    return options
