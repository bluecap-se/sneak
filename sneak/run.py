import sys
from sneak import cli
from sneak.stage import stage, TerminalTooSmallError
from sneak.game import graphics, gameloop


def run():
    try:
        options = cli.init()
        stage.create(options)

        # Raises TerminalTooSmallError if the chosen
        # size is larger than terminal window
        stage.validate()

        graphics.start()
        gameloop.start()

    except TerminalTooSmallError as e:
        sys.exit("ERROR: {}".format(e.message))

    except KeyboardInterrupt:
        graphics.exit()


if __name__ == "__main__":
    run()
