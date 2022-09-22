# Sneak Game

[![PyPI](https://img.shields.io/pypi/v/sneak-game.svg)](https://pypi.python.org/pypi/sneak-game)
![Status](https://img.shields.io/badge/status-stable-brightgreen.svg)
![Python Version](https://img.shields.io/badge/python-3.10-blue.svg)
![Platform](https://img.shields.io/badge/platform-win%20%7C%20lin%20%7C%20osx-lightgrey.svg)
![Black](https://img.shields.io/badge/code%20style-black-000000.svg)
![License](https://img.shields.io/badge/license-MIT-blue.svg)

Snake game in the terminal.

![Game screenshot](https://raw.githubusercontent.com/bluecap-se/sneak/master/screenshot.png)

## Install

### Using a package manager

```bash
$ pip install sneak-game
```

### From source

This project relies on [Pipenv](https://docs.pipenv.org/), ensure that it is installed with `pip install pipenv` first.

```bash
$ git clone git@github.com:bluecap-se/sneak.git
$ cd sneak
$ pipenv install
$ pipenv shell
$ pipenv install -e .
```

## Usage

```bash
$ sneak -h

Sneak: A terminal snake game

Usage: sneak [options]

Options:
  -s SIZE, --size=SIZE  Game size (s | m | l)
  -h, --help            Show this help message and exit
  -v, --version         Show version and exit
```

## License

Published under [MIT License](https://github.com/bluecap-se/sneak/blob/master/LICENSE).

## Thanks to

This project was inspired by [python-console-snake](https://github.com/tancredi/python-console-snake).
