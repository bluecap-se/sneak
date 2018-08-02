# -*- coding: utf-8 -*-

"""
Sneak: A terminal snake game

Usage: run.py [options]

Options:
  -h, --help            show this help message and exit
  -s SIZE, --size=SIZE  Game size (s | m | l)
  -f, --fullscreen      Play fullscreen

"""

from docopt import docopt

from optparse import OptionParser

options = None


def init():
    global options

    arguments = docopt(__doc__, version='TODO', options_first=True)

    options = {
        'size': arguments.get('--size', False) or 'm',
        'fullscreen': arguments.get('--fullscreen', False) or False,
    }

    return options
