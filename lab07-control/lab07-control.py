""" Lab 7 - User Control """

import arcade
import math

# --- Constants ---
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


class Ship:
    def __init__(self, position_x, position_y, size, orientation, color, change_x=0, change_y=0):

        # Take the parameters of the init function above, and create instance variables out of them.
        self.position_x = position_x
        self.position_y = position_y
        self.change_x = change_x
        self.change_y = change_y
        self.size = size
        self.orientation = orientation
        self.color = color
        self.points = [
            [self.position_x + self.size * math.cos(self.orientation),
             self.position_y + self.size * math.sin(self.orientation)],
            [self.position_x + self.size * math.cos(self.orientation + math.pi * 7 / 4),
             self.position_y + self.size * math.sin(self.orientation + math.pi * 7 / 4)],
            [self.position_x,
             self.position_y],
            [self.position_x + self.size * math.cos(self.orientation + math.pi * 9 / 4),
             self.position_y + self.size * math.sin(self.orientation + math.pi * 9 / 4)]]

    def draw(self):
        """ Draw the balls with the instance variables we have. """
        arcade.draw_polygon_filled(self.points, self.color)

    def upd_orientation(self, x, y):
        x_ = x - self.position_x
        y_ = y - self.position_y
        length = math.sqrt(x_ ** 2 + y_ ** 2)
        x_ /= length
        y_ /= length
        if y_ > 0:
            self.orientation = math.acos(x_)
        else:
            self.orientation = -math.acos(x_)

    def upd_position(self):
        # Move the ball
        self.position_y += self.change_y
        self.position_x += self.change_x

        # See if the ball hit the edge of the screen. If so, change direction
        if self.position_x < self.size:
            self.position_x = self.size
        if self.position_x > SCREEN_WIDTH - self.size:
            self.position_x = SCREEN_WIDTH - self.size
        if self.position_y < self.size:
            self.position_y = self.size
        if self.position_y > SCREEN_HEIGHT - self.size:
            self.position_y = SCREEN_HEIGHT - self.size

        self.points = [[self.position_x + self.size * math.cos(self.orientation),
                        self.position_y + self.size * math.sin(self.orientation)],
                       [self.position_x - self.size * math.cos(self.orientation + math.pi / 4),
                        self.position_y - self.size * math.sin(self.orientation + math.pi / 4)],
                       [self.position_x,
                        self.position_y],
                       [self.position_x - self.size * math.cos(self.orientation - math.pi / 4),
                        self.position_y - self.size * math.sin(self.orientation - math.pi / 4)]]


class MyGame(arcade.Window):
    """ Our Custom Window Class"""

    def __init__(self):
        """ Initializer """
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Lab 7 - User Control")
        self.set_update_rate(1/60)

        self.player = Ship(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, 10, 0, arcade.color.RED)
        self.speed = 250
        self.mouse_pos = [0, 0]
        self.mov_ud = ""
        self.mov_lr = ""

        self.pew = arcade.sound.load_sound("Sounds/pew.mp3")

    def on_draw(self):
        arcade.start_render()
        self.player.draw()

    def on_update(self, delta_time: float):
        if self.mov_ud == "up":
            self.player.change_y = self.speed * delta_time
        elif self.mov_ud == "down":
            self.player.change_y = -self.speed * delta_time
        if self.mov_lr == "right":
            self.player.change_x = self.speed * delta_time
        elif self.mov_lr == "left":
            self.player.change_x = -self.speed * delta_time
        self.player.upd_position()
        self.player.upd_orientation(self.mouse_pos[0], self.mouse_pos[1])

    def on_key_press(self, symbol: int, modifiers: int):
        if symbol == arcade.key.W:
            self.mov_ud = "up"
        elif symbol == arcade.key.A:
            self.mov_lr = "left"
        elif symbol == arcade.key.S:
            self.mov_ud = "down"
        elif symbol == arcade.key.D:
            self.mov_lr = "right"

    def on_key_release(self, symbol: int, modifiers: int):
        if symbol == arcade.key.W and self.mov_ud == "up":
            self.mov_ud = ""
            self.player.change_y = 0
        elif symbol == arcade.key.S and self.mov_ud == "down":
            self.mov_ud = ""
            self.player.change_y = 0
        elif symbol == arcade.key.A and self.mov_lr == "left":
            self.mov_lr = ""
            self.player.change_x = 0
        elif symbol == arcade.key.D and self.mov_lr == "right":
            self.mov_lr = ""
            self.player.change_x = 0

    def on_mouse_motion(self, x: float, y: float, dx: float, dy: float):
        self.mouse_pos = [x, y]

    def on_mouse_press(self, x: float, y: float, button: int, modifiers: int):
        if button == arcade.MOUSE_BUTTON_LEFT:
            arcade.sound.play_sound(self.pew)


def main():
    window = MyGame()
    arcade.run()


main()
