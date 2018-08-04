# -*- coding: utf-8 -*-

import curses
import math

import config

from terminal import Terminal


class TerminalTooSmallError(Exception):
    pass


class Stage:

    size = None
    width = None
    height = None
    padding = None

    def create(self, options={}):

        available_size = (width, height) = Terminal().get_size()

        chosen_size = config.game_sizes[options.get('size', 'm')]

        if chosen_size[0] > available_size[0] / 2:
            width = available_size[0] / 2
        else:
            width = chosen_size[0]

        if chosen_size[1] > available_size[1]:
            height = available_size[1]
        else:
            height = chosen_size[1]

        padding_x = int(math.floor(available_size[0] - width) / 4)
        padding_y = int(math.floor(available_size[1] - height) / 2)

        self.size = (width, height)
        self.chosen_size = chosen_size
        self.width = width
        self.height = height
        self.padding = (padding_y, padding_x, padding_y, padding_x)

    def validate(self):
        """
        Validates that the selected game size will fit
        inside the available space of the terminal window

        Raises `TerminalTooSmallError` error on validation failure.
        """
        if self.chosen_size[0] > self.width or \
           self.chosen_size[1] > self.height:
            raise TerminalTooSmallError('Chose a smaller size or increase terminal window.')

    @property
    def size(self):
        return self.size

    @property
    def width(self):
        return self.width

    @property
    def height(self):
        return self.height

    @property
    def padding(self):
        return self.padding

    @property
    def boundaries(self):
        return {
            'bottom': int(math.floor(self.height / 2)),
            'left': int(math.floor(-self.width / 2)),
            'right': int(math.floor(self.width / 2)),
            'top': int(math.floor(-self.height / 2)),
        }

    @property
    def chosen_theme(self):
        return {
            'colors': {
                'default': (curses.COLOR_WHITE, curses.COLOR_BLACK),
                'bg': (curses.COLOR_WHITE, curses.COLOR_WHITE),
                'snake': (curses.COLOR_RED, curses.COLOR_GREEN),
                'apple': (curses.COLOR_RED, curses.COLOR_RED),
                'border': (curses.COLOR_WHITE, curses.COLOR_YELLOW),
                'lives': (curses.COLOR_RED, curses.COLOR_RED),
                'text': (curses.COLOR_BLACK, curses.COLOR_WHITE),
            },
            'tiles': {
            }
        }

stage = Stage()
