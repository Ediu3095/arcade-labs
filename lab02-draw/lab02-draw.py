import arcade

arcade.open_window(600, 600, "Dwarf Fortress logo")

arcade.set_background_color(arcade.color.BATTLESHIP_GREY)

arcade.start_render()



arcade.draw_circle_filled(300, 300, 160, arcade.color.BRONZE)

arcade.draw_polygon_filled([[380, 380],
                            [360, 260],
                            [220, 240],
                            [318, 141],
                            [391, 168],
                            [439, 220],
                            [460, 300]], (185, 97, 30))

arcade.draw_circle_outline(300, 300, 160, arcade.color.BLACK, 20)

arcade.draw_rectangle_filled(270, 330, 20, 20, arcade.color.BLACK)
arcade.draw_rectangle_filled(330, 330, 20, 20, arcade.color.BLACK)
arcade.draw_polygon_filled([[360, 380],
                            [360, 300],
                            [320, 300],
                            [320, 280],
                            [340, 280],
                            [340, 260],
                            [320, 260],
                            [320, 300],
                            [280, 300],
                            [280, 260],
                            [260, 260],
                            [260, 280],
                            [280, 280],
                            [279, 300],
                            [240, 300],
                            [240, 380],
                            [220, 380],
                            [220, 240],
                            [240, 240],
                            [240, 220],
                            [280, 220],
                            [280, 200],
                            [300, 200],
                            [300, 180],
                            [340, 180],
                            [340, 240],
                            [360, 240],
                            [360, 260],
                            [380, 260],
                            [380, 380]], arcade.color.BLACK)

arcade.draw_rectangle_filled(300, 390, 120, 20, arcade.color.BLACK)



arcade.finish_render()



arcade.run()
