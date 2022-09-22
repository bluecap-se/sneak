import curses
from sneak.stage import stage


class Theme:
    colors_map = {}
    theme = None

    def __init__(self):
        self.theme = stage.chosen_theme
        self.colors_map = self.get_colors_map()

    def get_color(self, key):
        return curses.color_pair(self.colors_map.get(key, 0))

    def get_tile(self, key):
        return self.theme["tiles"].get(key, " ")

    def get_colors_map(self):
        out = {}
        i = 1

        for col in self.theme["colors"].items():
            curses.init_pair(i, col[1][0], col[1][1])
            out[col[0]] = i
            i += 1

        return out
