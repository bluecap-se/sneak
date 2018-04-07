# Sneak Game

[![Travis](https://img.shields.io/travis/bluecap-se/sneak.svg)](https://travis-ci.org/bluecap-se/sneak)
[![Dependency Status](https://gemnasium.com/bluecap-se/sneak.svg)](https://gemnasium.com/bluecap-se/sneak)
[![PyPI](https://img.shields.io/pypi/v/sneak-game.svg)](https://pypi.python.org/pypi/sneak-game)

Snake game in the terminal.

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
