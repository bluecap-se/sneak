import os
import platform
import shlex
import struct
import subprocess


class Terminal:
    def get_size(self):
        """
        Gets terminal window size

         - get width and height of console
         - works on linux, os x, windows, cygwin (windows)

        From: http://stackoverflow.com/questions/566746/how-to-get-console-window-width-in-python

        :return: Tuple, (width, height)
        """
        current_os = platform.system()
        tuple_xy = None

        if current_os == "Windows":
            tuple_xy = self.get_size_windows()

            if not tuple_xy:
                tuple_xy = self.get_size_tput()

        # needed for window's python in cygwin's xterm!
        if current_os in ["Linux", "Darwin"] or current_os.startswith("CYGWIN"):
            tuple_xy = self.get_size_linux()

        if not tuple_xy:
            tuple_xy = (80, 25)  # default value

        return tuple_xy

    @staticmethod
    def get_size_windows():
        try:
            from ctypes import windll, create_string_buffer

            # stdin handle is -10
            # stdout handle is -11
            # stderr handle is -12
            h = windll.kernel32.GetStdHandle(-12)
            csbi = create_string_buffer(22)
            res = windll.kernel32.GetConsoleScreenBufferInfo(h, csbi)
            if res:
                (
                    bufx,
                    bufy,
                    curx,
                    cury,
                    wattr,
                    left,
                    top,
                    right,
                    bottom,
                    maxx,
                    maxy,
                ) = struct.unpack("hhhhHhhhhhh", csbi.raw)
                sizex = right - left + 1
                sizey = bottom - top + 1
                return sizex, sizey
        except:
            pass

    @staticmethod
    def get_size_tput():
        # get terminal width
        # src: http://stackoverflow.com/questions/263890/how-do-i-find-the-width-height-of-a-terminal-window
        try:
            cols = int(subprocess.check_call(shlex.split("tput cols")))
            rows = int(subprocess.check_call(shlex.split("tput lines")))
            return (cols, rows)
        except:
            pass

    @staticmethod
    def get_size_linux():
        def ioctl_GWINSZ(fd):
            try:
                import fcntl
                import termios

                cr = struct.unpack("hh", fcntl.ioctl(fd, termios.TIOCGWINSZ, "1234"))
                return cr
            except:
                pass

        cr = ioctl_GWINSZ(0) or ioctl_GWINSZ(1) or ioctl_GWINSZ(2)

        if not cr:
            try:
                fd = os.open(os.ctermid(), os.O_RDONLY)
                cr = ioctl_GWINSZ(fd)
                os.close(fd)
            except:
                pass

        if not cr:
            try:
                cr = (os.environ["LINES"], os.environ["COLUMNS"])
            except:
                return None

        return int(cr[1]), int(cr[0])
