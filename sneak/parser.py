# -*- coding: utf-8 -*-

from docopt import docopt

from __init__ import __doc__, __version__


def init():

    arguments = docopt(__doc__, version='v{}'.format(__version__), options_first=True)

    options = {
        'size': arguments.get('--size', False) or 'm',
    }

    return options
