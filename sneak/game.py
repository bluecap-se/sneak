import __main__
import curses
import math
import time
import random
from sneak import config
from sneak.theme import Theme
from sneak.stage import stage


class Game:

    direction = (0, 0)
    lastPos = (0, 0)
    snake = []
    speed = 1
    apples = []
    grow = config.initial_size - 1
    score = 0
    lives = 3

    def start(self):
        self.reset()
        self.score = 0
        self.lives = 3

    def update(self):
        self.move_snake()
        self.check_catch()
        self.check_position_allowed()

    def check_catch(self):
        if not len(self.snake) or not len(self.apples):
            return

        for i, apple in enumerate(self.apples):
            if self.snake[0][0] == apple[0] and self.snake[0][1] == apple[1]:
                self.eat_apple(i)

    def eat_apple(self, i):
        self.apples.pop(i)
        self.spawn_apple()
        self.grow += config.food_values["apple"]
        self.score += 1

    def move_snake(self):
        last_unchanged = None
        self.lastPos = (
            self.snake[len(self.snake) - 1][0],
            self.snake[len(self.snake) - 1][1],
        )

        for i, part in enumerate(self.snake):
            if i == 0:
                x = part[0] + self.speed * self.direction[0]
                y = part[1] + self.speed * self.direction[1]
            else:
                x = last_unchanged[0]
                y = last_unchanged[1]

            last_unchanged = (self.snake[i][0], self.snake[i][1])
            self.snake[i] = (x, y)

        if self.grow:
            self.snake.append(last_unchanged)
            self.grow -= 1

    def get_game_area(self):
        w = math.fabs(stage.boundaries["right"] - stage.boundaries["left"])
        h = math.fabs(stage.boundaries["top"] - stage.boundaries["bottom"])

        return int(math.floor(w * h))

    def reset(self):
        self.direction = (1, 0)
        self.snake = [(0, 0)]
        gameloop.frame = 1
        self.apples_count = 1
        self.apples = []
        self.grow = config.initial_size - 1

        self.apples_count += int(math.floor(self.get_game_area() / config.apple_domain))

        for i in range(0, self.apples_count):
            self.spawn_apple()

    def spawn_apple(self):
        if len(self.apples) >= self.get_game_area():
            return

        x = random.randrange(stage.boundaries["left"], stage.boundaries["right"])
        y = random.randrange(stage.boundaries["top"], stage.boundaries["bottom"])

        position_free = True

        for apple in self.apples:
            if apple[0] == x and apple[1] == y:
                position_free = False

        for part in self.snake:
            if part[0] == x and part[1] == y:
                position_free = False

        if position_free and not self.is_out_of_boundaries(x, y):
            self.apples.append((x, y))
        else:
            self.spawn_apple()

    def is_out_of_boundaries(self, x, y):
        if x < stage.boundaries["left"] or x > stage.boundaries["right"] - 1:
            return True

        elif y < stage.boundaries["top"] or y > stage.boundaries["bottom"] - 1:
            return True

        return False

    def check_position_allowed(self):
        collides_with_body = False
        x = self.snake[0][0]
        y = self.snake[0][1]

        for i in range(1, len(self.snake) - 1):
            if x == self.snake[i][0] and y == self.snake[i][1]:
                collides_with_body = True
                break

        if collides_with_body or self.is_out_of_boundaries(x, y):
            gameloop.reset()
            self.lives -= 1
            if self.lives == 0:
                gameloop.state = 1


class Gameloop:

    last_update = None
    playing = False
    state = 0

    def init(self):
        game.start()
        graphics.draw_game()
        self.state = 0

    def update(self):
        game.update()
        graphics.update()

    def step(self):
        cur_time = time.time()

        if self.last_update:
            elapsed = cur_time - self.last_update
        else:
            elapsed = 0

        if not elapsed or elapsed > config.frame_len:

            if not elapsed:
                until_next = config.frame_len
            else:
                until_next = elapsed - config.frame_len
                time.sleep(until_next)

            self.update()
            self.last_update = time.time()

    def start(self):
        self.playing = True
        self.init()

        while self.playing:
            self.update_controls()
            if self.state == 0:
                self.step()
            elif self.state == 1:
                graphics.draw_game_over()

    def stop(self):
        self.playing = False

    def update_controls(self):
        key = graphics.screen.getch()
        keys = config.keys

        if key > 0:
            if key == keys["DOWN"]:
                if game.direction[1] == -1:
                    return

                game.direction = (0, 1)

            elif key == keys["LEFT"]:
                if game.direction[0] == 1:
                    return

                game.direction = (-1, 0)

            elif key == keys["RIGHT"]:
                if game.direction[0] == -1:
                    return

                game.direction = (1, 0)

            elif key == keys["UP"]:
                if game.direction[1] == 1:
                    return

                game.direction = (0, -1)

            elif key == keys["Q"]:
                self.playing = False
                graphics.exit()

            elif self.state == 1 and key == keys["ENTER"]:
                self.init()

    def reset(self):
        game.reset()
        graphics.draw_game()


class Graphics:

    screen = None
    theme = None

    def start(self):
        self.screen = curses.initscr()
        curses.noecho()
        curses.cbreak()
        curses.curs_set(0)
        curses.start_color()
        self.screen.nodelay(1)

        # Needs to be done after `initscr()` call
        self.theme = Theme()

    def draw_tile(self, x, y, tile="", color=None):
        color = color or self.theme.get_color("default")

        x = int(x * 2 + stage.padding[3] * 2 + stage.width / 2)
        y += stage.padding[0] + stage.height / 2
        y = int(y)

        self.screen.addstr(y, x, tile, color)
        if len(tile) < 2:
            self.screen.addstr(y, x + 1, tile, color)

    def draw_game_over(self):
        self.draw_tile(-4, -1, " GAME OVER ", self.theme.get_color("text"))
        self.draw_tile(-7, 1, " Press ENTER to restart ", self.theme.get_color("text"))

    def draw_score(self):
        score_formatted = str(game.score).zfill(2)

        self.draw_tile(
            (stage.width / 2) - 1,
            (-stage.height / 2) - 1,
            score_formatted,
            self.theme.get_color("text"),
        )

    def draw_lives(self):
        posx = (-stage.width / 2) + 3

        for x in range(1, game.lives + 1):
            posx += 1
            self.draw_tile(
                posx,
                (-stage.height / 2) - 1,
                self.theme.get_tile("lives"),
                self.theme.get_color("lives"),
            )
            posx += 1
            self.draw_tile(
                posx,
                (-stage.height / 2) - 1,
                self.theme.get_tile("border-h"),
                self.theme.get_color("border"),
            )

    def draw_snake(self):
        for part in game.snake:
            self.draw_tile(
                part[0],
                part[1],
                self.theme.get_tile("snake-body"),
                self.theme.get_color("snake"),
            )

        # Clean last tile
        self.draw_tile(
            game.lastPos[0],
            game.lastPos[1],
            self.theme.get_tile("bg"),
            self.theme.get_color("bg"),
        )

    def draw_apples(self):
        for apple in game.apples:
            self.draw_tile(
                apple[0],
                apple[1],
                self.theme.get_tile("apple"),
                self.theme.get_color("apple"),
            )

    def draw_game(self):
        for y in range(stage.boundaries["top"], stage.boundaries["bottom"]):
            for x in range(stage.boundaries["left"], stage.boundaries["right"]):
                self.draw_tile(
                    x, y, self.theme.get_tile("bg"), self.theme.get_color("bg")
                )

        self.draw_borders()
        self.draw_text()

    def draw_borders(self):
        tile_v = self.theme.get_tile("border-v")
        tile_h = self.theme.get_tile("border-h")
        tile_c = self.theme.get_tile("border-c")
        color = self.theme.get_color("border")

        x_left = stage.boundaries["left"]
        x_right = stage.boundaries["right"]

        y_top = stage.boundaries["top"]
        y_bottom = stage.boundaries["bottom"]

        for y in range(y_top, y_bottom):
            self.draw_tile(x_left - 1, y, tile_v, color)
            self.draw_tile(x_right, y, tile_v, color)

        for x in range(x_left, x_right):
            self.draw_tile(x, y_top - 1, tile_h, color)
            self.draw_tile(x, y_bottom, tile_h, color)

        self.draw_tile(x_left - 1, y_top - 1, tile_c, color)
        self.draw_tile(x_left - 1, y_bottom, tile_c, color)
        self.draw_tile(x_right, y_top - 1, tile_c, color)
        self.draw_tile(x_right, y_bottom, tile_c, color)

    def draw_text(self):
        color = self.theme.get_color("text")

        self.draw_tile((stage.width / 2) - 4, (-stage.height / 2) - 1, "score:", color)
        self.draw_tile((-stage.width / 2), (-stage.height / 2) - 1, "lives:", color)
        self.draw_tile(-5, (stage.height / 2), " Press Q to quit ", color)

    def update(self):
        self.draw_snake()
        self.draw_apples()
        self.draw_score()
        self.draw_lives()

    def exit(self):
        self.screen.clear()
        self.screen.keypad(0)
        curses.echo()
        curses.nocbreak()
        curses.endwin()


game = Game()
gameloop = Gameloop()
graphics = Graphics()
