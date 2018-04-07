# Sneak Game

[![Travis](https://img.shields.io/travis/bluecap-se/sneak.svg)](https://travis-ci.org/bluecap-se/sneak)
[![Coverage](https://img.shields.io/coveralls/github/bluecap-se/sneak.svg)](https://coveralls.io/github/bluecap-se/sneak?branch=develop)
[![Dependency Status](https://gemnasium.com/bluecap-se/sneak.svg)](https://gemnasium.com/bluecap-se/sneak)
[![PyPI](https://img.shields.io/pypi/v/sneak-game.svg)](https://pypi.python.org/pypi/sneak-game)
![Status](https://img.shields.io/badge/status-stable-brightgreen.svg)
![PyPI - Python Version](https://img.shields.io/badge/python-2.7-blue.svg)
![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Platform](https://img.shields.io/badge/platform-win%20%7C%20lin%20%7C%20osx-lightgrey.svg)

Snake game in the terminal.

![Game screenshot](/screenshot.png)

## Install

### Using a package manager

```bash
$ pip install sneak
```

### From source

```bash
$ git clone git@github.com:bluecap-se/sneak.git
$ cd sneak
$ pip install -r requirements.txt
$ pip install -e .
```

## Usage

```bash
$ sneak -h

Sneak - snake game in the terminal

Usage:
      sneak [options]

Options:
  -h, --help                Output this help and exit
  --version                 Output version and exit

```


## Run tests

### Regular tests

```bash
$ pip install -r requirements_test.txt
$ py.test
```

### Watch for changes

To run the tests continuously, run the test command with the watch or follow flag `-f`:

```bash
$ py.test -f
```

### Test coverage

```console
$ coverage run --source sneak -m py.test
$ coverage html
$ open htmlcov/index.html
```

## License

Published under [MIT License](https://github.com/bluecap-se/sneak/blob/master/LICENSE).

## Thanks to

This project was inspired by [python-console-snake](https://github.com/tancredi/python-console-snake).
