# -*- coding: utf-8 -*-

import __main__
import time

import config
import game
import graphics


def update_controls():
    key = graphics.screen.getch()
    keys = config.keys

    if key > 0:
        if key == keys['DOWN']:
            if game.direction[1] == -1:
                return

            game.direction = (0, 1)

        elif key == keys['LEFT']:
            if game.direction[0] == 1:
                return

            game.direction = (-1, 0)

        elif key == keys['RIGHT']:
            if game.direction[0] == -1:
                return

            game.direction = (1, 0)

        elif key == keys['UP']:
            if game.direction[1] == 1:
                return

            game.direction = (0, -1)

        elif key == keys['Q']:
            __main__.exit()
            exit()

        elif state == 1 and key == keys['ENTER']:
            init()


last_update = None
playing = False
state = 0
global_stage = None


def update():
    game.update()
    graphics.update()


def step():
    global last_update

    cur_time = time.time()

    if last_update:
        elapsed = cur_time - last_update
    else:
        elapsed = 0

    if not elapsed or elapsed > config.frame_len:

        if not elapsed:
            until_next = config.frame_len
        else:
            until_next = elapsed - config.frame_len
            time.sleep(until_next)

        update()
        last_update = time.time()


def start(stage):
    global playing, state

    playing = True

    init(stage)
    while playing:
        update_controls()
        if state == 0:
            step()
        elif state == 1:
            graphics.drawGameOver()


def stop():
    global playing, frame, last_update

    playing = False


def init(stage=None):
    global state, global_stage

    stg = stage or global_stage
    global_stage = stg

    game.init(stg)
    graphics.drawGame()
    state = 0


def reset():
    game.reset()
    graphics.drawGame()
