""" Lab 7 - User Control """

import arcade
import math
from random import randrange

# --- Constants ---
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


class MyGame(arcade.Window):
    """ Our Custom Window Class"""

    def __init__(self):
        """ Initializer """
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Lab 7 - User Control")
        self.set_update_rate(1 / 60)

        self.player = arcade.Sprite("Sprites/Particle.png", 1)
        self.score = 0

        self.good = arcade.SpriteList()
        self.good_max_amount = 10
        self.good_x = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.good_y = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

        self.bad = arcade.SpriteList()
        self.bad_max_amount = 10
        self.bad_x = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.bad_y = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

        # Sounds
        self.good_sound = arcade.Sound("Sounds/270304__littlerobotsoundfactory__collect-point-00.wav")
        self.bad_sound = arcade.Sound("Sounds/270332__littlerobotsoundfactory__hit-03.wav")

        # Background
        pass

        # Mouse
        self.set_mouse_visible(False)

    def setup(self):
        for i in range(self.good_max_amount):
            self.good.append(arcade.Sprite("Sprites/Proton.png", 1, center_x=randrange(SCREEN_WIDTH),
                                           center_y=randrange(SCREEN_HEIGHT)))
            self.good_x[i] = randrange(-8, 8, 1)
            self.good_y[i] = randrange(-8, 8, 1)
        for i in range(self.bad_max_amount):
            self.bad.append(arcade.Sprite("Sprites/Electron.png", 1, center_x=randrange(SCREEN_WIDTH),
                                          center_y=randrange(SCREEN_HEIGHT)))
            self.bad_x[i] = randrange(-8, 8, 1)
            self.bad_y[i] = randrange(-8, 8, 1)

    def on_draw(self):
        arcade.start_render()
        self.player.draw()
        self.good.draw()
        self.bad.draw()
        arcade.draw_text("Score: " + str(self.score), 0, 0, arcade.color.WHITE, font_size=20)

    def on_update(self, delta_time: float):
        self.upd_particles()
        self.handle_collisions(self.good, self.good_x, self.good_y, self.good_sound, 1)
        self.handle_collisions(self.bad, self.bad_x, self.bad_y, self.bad_sound, -1)

    @staticmethod
    def pos_update(sprite: arcade.Sprite, speed_x, speed_y):
        # x axis
        sprite.center_x += speed_x
        if sprite.center_x >= SCREEN_WIDTH:
            sprite.center_x = 1
        elif sprite.center_x <= 0:
            sprite.center_x = SCREEN_WIDTH - 1
        # y axis
        sprite.center_y += speed_y
        if sprite.center_y >= SCREEN_HEIGHT:
            sprite.center_y = 1
        elif sprite.center_y < 0:
            sprite.center_y = SCREEN_HEIGHT - 1

    def upd_particles(self):
        i = 0
        for elem in self.good:
            self.pos_update(elem, self.good_x[i], self.good_y[i])
            i += 1
        i = 0
        for elem in self.bad:
            self.pos_update(elem, self.bad_x[i], self.bad_y[i])
            i += 1

    def handle_collisions(self, s_list: arcade.SpriteList, x: list, y: list, sound: arcade.Sound, score_mod: int):
        i = 0
        for elem in s_list:
            if elem.collides_with_sprite(self.player):
                self.score += score_mod
                elem.center_x, elem.center_y = randrange(SCREEN_WIDTH), randrange(SCREEN_HEIGHT)
                x[i] = randrange(-4, 4, 1)
                y[i] = randrange(-4, 4, 1)
                sound.play()

    def on_mouse_motion(self, x: float, y: float, dx: float, dy: float):
        self.player.center_x = x
        self.player.center_y = y


def main():
    window = MyGame()
    window.setup()
    arcade.run()


main()
