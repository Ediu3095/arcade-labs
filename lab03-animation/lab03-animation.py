import arcade
import math
from random import randrange


class MyGame(arcade.Window):

    def __init__(self, width, height, title, Cx, Cy, Sx, Sy):
        super().__init__(width, height, title)
        self.centreX = Cx
        self.centreY = Cy
        self.speedX = Sx
        self.speedY = Sy
        self.rotation = 0
        self.framerate = [0 for i in range(30)]
        self.set_update_rate(1 / 60)
        arcade.set_background_color(arcade.color.BATTLESHIP_GREY)
        self.f3 = 0
        self.f5 = False

    def averageFPS(self):
        FPS = 0
        for elem in self.framerate:
            FPS += elem / len(self.framerate)
        return int(FPS)

    def FPShift(self, new_framerate):
        for i in range(len(self.framerate) - 1):
            self.framerate[i] = self.framerate[i + 1]
        self.framerate[len(self.framerate) - 1] = new_framerate

    def rose_of_wind_white(self, rotation=0, radius_small=80, radius_large=330):
        arcade.draw_polygon_filled(
            [[math.cos(rotation) * radius_small + self.centreX, math.sin(rotation) * radius_small + self.centreY],
             [math.cos(rotation + math.pi / 4) * radius_large + self.centreX,
              math.sin(rotation + math.pi / 4) * radius_large + self.centreY],
             [math.cos(rotation + math.pi / 2) * radius_small + self.centreX,
              math.sin(rotation + math.pi / 2) * radius_small + self.centreY],
             [math.cos(rotation + 3 * math.pi / 4) * radius_large + self.centreX,
              math.sin(rotation + 3 * math.pi / 4) * radius_large + self.centreY],
             [math.cos(rotation + math.pi) * radius_small + self.centreX,
              math.sin(rotation + math.pi) * radius_small + self.centreY],
             [math.cos(rotation + 5 * math.pi / 4) * radius_large + self.centreX,
              math.sin(rotation + 5 * math.pi / 4) * radius_large + self.centreY],
             [math.cos(rotation + 3 * math.pi / 2) * radius_small + self.centreX,
              math.sin(rotation + 3 * math.pi / 2) * radius_small + self.centreY],
             [math.cos(rotation + 7 * math.pi / 4) * radius_large + self.centreX,
              math.sin(rotation + 7 * math.pi / 4) * radius_large + self.centreY]],
            arcade.color.WHITE)

    def rose_of_wind_black(self, rotation=0, radius_small=80, radius_large=330):
        arcade.draw_circle_outline(self.centreX, self.centreY, radius_large, arcade.color.BLACK, radius_large / 38)
        arcade.draw_circle_outline(self.centreX, self.centreY, radius_large - 60, arcade.color.BLACK,
                                   radius_large / 19)
        arcade.draw_polygon_filled(
            [[math.cos(rotation) * radius_large + self.centreX, math.sin(rotation) * radius_large + self.centreY],
             [math.cos(rotation + math.pi / 4) * radius_small + self.centreX,
              math.sin(rotation + math.pi / 4) * radius_small + self.centreY],
             [math.cos(rotation + math.pi / 2) * radius_large + self.centreX,
              math.sin(rotation + math.pi / 2) * radius_large + self.centreY],
             [math.cos(rotation + 3 * math.pi / 4) * radius_small + self.centreX,
              math.sin(rotation + 3 * math.pi / 4) * radius_small + self.centreY],
             [math.cos(rotation + math.pi) * radius_large + self.centreX,
              math.sin(rotation + math.pi) * radius_large + self.centreY],
             [math.cos(rotation + 5 * math.pi / 4) * radius_small + self.centreX,
              math.sin(rotation + 5 * math.pi / 4) * radius_small + self.centreY],
             [math.cos(rotation + 3 * math.pi / 2) * radius_large + self.centreX,
              math.sin(rotation + 3 * math.pi / 2) * radius_large + self.centreY],
             [math.cos(rotation + 7 * math.pi / 4) * radius_small + self.centreX,
              math.sin(rotation + 7 * math.pi / 4) * radius_small + self.centreY]],
            arcade.color.BLACK)

    def dwarf_fortress(self):
        arcade.draw_circle_filled(self.centreX, self.centreY, 160, arcade.color.BRONZE)

        arcade.draw_polygon_filled([[self.centreX + 80, self.centreY + 80],
                                    [self.centreX + 59, self.centreY - 39],
                                    [self.centreX - 80, self.centreY - 60],
                                    [self.centreX + 18, self.centreY - 159],
                                    [self.centreX + 91, self.centreY - 132],
                                    [self.centreX + 139, self.centreY - 80],
                                    [self.centreX + 160, self.centreY]], (185, 97, 30))

        arcade.draw_circle_outline(self.centreX, self.centreY, 160, arcade.color.BLACK, 20)

        arcade.draw_rectangle_filled(self.centreX - 30, self.centreY + 30, 20, 20, arcade.color.BLACK)
        arcade.draw_rectangle_filled(self.centreX + 30, self.centreY + 30, 20, 20, arcade.color.BLACK)
        arcade.draw_polygon_filled([[self.centreX + 60, self.centreY + 80],
                                    [self.centreX + 60, self.centreY],
                                    [self.centreX + 21, self.centreY],
                                    [self.centreX + 21, self.centreY - 20],
                                    [self.centreX + 40, self.centreY - 20],
                                    [self.centreX + 40, self.centreY - 40],
                                    [self.centreX + 20, self.centreY - 40],
                                    [self.centreX + 20, self.centreY],
                                    [self.centreX - 20, self.centreY],
                                    [self.centreX - 20, self.centreY - 40],
                                    [self.centreX - 40, self.centreY - 40],
                                    [self.centreX - 40, self.centreY - 20],
                                    [self.centreX - 21, self.centreY - 20],
                                    [self.centreX - 21, self.centreY],
                                    [self.centreX - 60, self.centreY],
                                    [self.centreX - 60, self.centreY + 80],
                                    [self.centreX - 80, self.centreY + 80],
                                    [self.centreX - 80, self.centreY - 60],
                                    [self.centreX - 60, self.centreY - 60],
                                    [self.centreX - 60, self.centreY - 80],
                                    [self.centreX - 20, self.centreY - 80],
                                    [self.centreX - 20, self.centreY - 100],
                                    [self.centreX, self.centreY - 100],
                                    [self.centreX, self.centreY - 120],
                                    [self.centreX + 40, self.centreY - 120],
                                    [self.centreX + 40, self.centreY - 60],
                                    [self.centreX + 60, self.centreY - 60],
                                    [self.centreX + 60, self.centreY - 40],
                                    [self.centreX + 80, self.centreY - 40],
                                    [self.centreX + 80, self.centreY + 80]], arcade.color.BLACK)

        arcade.draw_rectangle_filled(self.centreX, self.centreY + 90, 120, 20, arcade.color.BLACK)

    def on_draw(self):
        arcade.start_render()
        if self.f5:
            arcade.draw_text("Design inpired by Samuel Jiménez Rodero's \"Wind Rose\"", self.width / 2,
                             self.height - 27, arcade.color.BLACK, 20, bold=True, align="center", anchor_x="center")
            self.rose_of_wind_white(self.rotation, 40, 140)
            self.rose_of_wind_black(-self.rotation, 40, 160)
        else:
            self.dwarf_fortress()

        if self.f3 != 0:
            arcade.draw_text("FPS: " + str(self.averageFPS()), 2, self.height - 27, arcade.color.BLACK, 20, bold=True)
            arcade.draw_text("FPS: " + str(self.averageFPS()), 0, self.height - 25, arcade.color.WHITE, 20, bold=False)
            if self.f3 == 2:
                arcade.draw_rectangle_filled(len(self.framerate) * 5, 60, len(self.framerate) * 10, 120,
                                             arcade.color.WHITE)
                arcade.draw_rectangle_filled(len(self.framerate) * 5, self.averageFPS() * 2, len(self.framerate) * 10,
                                             1, arcade.color.RED)
                for i in range(len(self.framerate)):
                    arcade.draw_rectangle_filled(i * 10 + 5, self.framerate[i] * 2, 10, 1, arcade.color.BLACK)

    def on_update(self, delta_time):
        self.FPShift(int(1 // delta_time))
        self.rotation += 1 / 2 * delta_time
        self.centreX = self.centreX + (self.speedX * delta_time)
        self.centreY = self.centreY + (self.speedY * delta_time)
        if self.centreX + 170 > self.width:
            self.centreX = self.width - 170
            self.speedX *= -1
        if self.centreX - 170 < 0:
            self.centreX = 170
            self.speedX *= -1
        if self.centreY + 170 >= self.height:
            self.centreY = self.height - 170
            self.speedY *= -1
        if self.centreY - 170 <= 0:
            self.centreY = 170
            self.speedY *= -1

    def on_key_press(self, symbol, modifiers):
        if symbol == arcade.key.F3:
            self.f3 += 1
            if self.f3 == 3:
                self.f3 = 0

        if symbol == arcade.key.F5:
            self.f5 = not self.f5


Screen = MyGame(randrange(600, 1200), randrange(400, 800), "Dwarf Fortress logo", 300, 300, randrange(500),
                randrange(500))

arcade.run()
