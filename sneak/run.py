# -*- coding: utf-8 -*-

import sys

import graphics
import gameloop
import cli
import stage


def exit():
    graphics.exit()
    print 'Thank you, come again!'


def run():
    try:
        options = cli.init()
        stg = stage.Stage(options)

        # Raises TerminalTooSmallError if the chosen
        # size is larger than terminal window
        stg.validate()

        graphics.init(stg)
        gameloop.start(stg)

    except stage.TerminalTooSmallError as e:
        sys.exit('ERROR: {}'.format(e.message))

    except KeyboardInterrupt:
        exit()

if __name__ == '__main__':
    run()
