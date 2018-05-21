import os
import random
from PIL import Image
from PIL import ImageDraw

import coord_dicts as coords
import pallet_dicts as pallet

class SpriteDrawer(object):
    def __init__(self, rand_pal=False, rand_shapes=False,
                 spr_size=(16, 32), skin_color="light_1",
                 hair_color="brown_1", eye_color="brown_1",
                 top_color_5="green_grey_1", bottom_color="jeans_color_1",
                 shoe_color="brown_1", hair_style="hair_shaggy_1",
                 top_style="shirt_ls_1", hand_style="hands_idle_1",
                 bottom_style="jeans_skinny_1", shoe_style="shoes_boots_1"):
        self.im = Image.new("RGB", spr_size, (255, 255, 255))
        self.drawer = ImageDraw.Draw(self.im)
        self.color_attrs = ['skin_color', 'hair_color', 'eye_color',
                            'top_color_5', 'bottom_color', 'shoe_color']

        if not rand_pal:
            # Get Colors
            self.skin_color = pallet.skin_colors[f"{skin_color}"]
            self.hair_color = pallet.hair_colors[f"{hair_color}"]
            self.eye_color = pallet.eye_colors[f"{eye_color}"]
            self.top_color = pallet.top_colors_5[f"{top_color_5}"]
            self.bottom_color = pallet.bottom_colors[f"{bottom_color}"]
            self.shoe_color= pallet.shoe_colors[f"{shoe_color}"]
        else:
            # Randomly Choose Colors
            skin_color_c = random.choice(list(pallet.skin_colors.keys()))
            self.skin_color = pallet.skin_colors[f"{skin_color_c}"]
            hair_color_c = random.choice(list(pallet.hair_colors.keys()))
            self.hair_color = pallet.hair_colors[f"{hair_color_c}"]
            eye_color_c = random.choice(list(pallet.eye_colors.keys()))
            self.eye_color = pallet.eye_colors[f"{eye_color_c}"]
            top_color_c = random.choice(list(pallet.top_colors_5.keys()))
            self.top_color = pallet.top_colors_5[f"{top_color_c}"]
            bottom_color_c = random.choice(list(pallet.bottom_colors.keys()))
            self.bottom_color = pallet.bottom_colors[f"{bottom_color_c}"]
            shoe_color_c = random.choice(list(pallet.shoe_colors.keys()))
            self.shoe_color = pallet.shoe_colors[f"{shoe_color_c}"]


        if not rand_shapes:
            # Get Shapes
            self.head = coords.heads["head_1"]
            self.eye_style = coords.eyes["eyes_1"]
            self.hair_style = coords.hair_style[f"{hair_style}"]
            self.top_style = coords.top_style[f"{top_style}"]
            self.hand_style = coords.hand_style[f"{hand_style}"]
            self.bottom_style = coords.bottom_style[f"{bottom_style}"]
            self.shoe_style = coords.shoe_style[f"{shoe_style}"]
        else:
            self.head = coords.heads["head_1"]
            self.eye_style = coords.eyes["eyes_1"]
            hair_style_c = random.choice(list(coords.hair_style.keys()))
            self.hair_style = coords.hair_style[f"{hair_style_c}"]
            top_style_c = random.choice(list(coords.top_style.keys()))
            self.top_style = coords.top_style[f"{top_style_c}"]
            hand_style_c = random.choice(list(coords.hand_style.keys()))
            self.hand_style = coords.hand_style[f"{hand_style_c}"]
            while True:
                bottom_style_c = random.choice(list(coords.bottom_style.keys()))
                if bottom_style_c != "plain_legs_1":
                    break
            self.bottom_style = coords.bottom_style[f"{bottom_style_c}"]
            shoe_style_c = random.choice(list(coords.shoe_style.keys()))
            self.shoe_style = coords.shoe_style[f"{shoe_style_c}"]

        if not os.path.exists("./sprites/"):
            os.mkdir("./sprites/")

        self.draw_head()
        self.draw_hair()
        self.draw_eyes()
        self.draw_hands()
        if top_style_c == "dress_short_1" or top_style_c == "dress_short_2":
            self.bottom_style = coords.bottom_style["plain_legs_1"]
            self.bottom_color = self.skin_color
            self.draw_bottom()
            self.draw_top()
        else:
            self.draw_top()
            self.draw_bottom()
        self.draw_shoes()
        self.im.save("./sprites/test.png")


    def draw_head(self):

        for color_coord in self.head.items():
            color = int(color_coord[0][-1])
            coords = color_coord[1]
            for coord in coords:
                self.drawer.point(coord, self.skin_color[color])


    def draw_hair(self):

        for color_coord in self.hair_style.items():
            color = int(color_coord[0][-1])
            coords = color_coord[1]
            for coord in coords:
                self.drawer.point(coord, self.hair_color[color])


    def draw_eyes(self):

        for color_coord in self.eye_style.items():
            color = int(color_coord[0][-1])
            coords = color_coord[1]
            for coord in coords:
                self.drawer.point(coord, self.eye_color[color])


    def draw_hands(self):

        for color_coord in self.hand_style.items():
            color = int(color_coord[0][-1])
            coords = color_coord[1]
            for coord in coords:
                if color == 1:
                    color = color + 1
                self.drawer.point(coord, self.skin_color[color])


    def draw_top(self):

        for color_coord in self.top_style.items():
            color = int(color_coord[0][-1])
            coords = color_coord[1]
            for coord in coords:
                self.drawer.point(coord, self.top_color[color])


    def draw_bottom(self):

        for color_coord in self.bottom_style.items():
            color = int(color_coord[0][-1])
            coords = color_coord[1]
            for coord in coords:
                try:
                    self.drawer.point(coord, self.bottom_color[color])
                except IndexError:
                    self.drawer.point(coord, self.top_color[color - 1])



    def draw_shoes(self):

        for color_coord in self.shoe_style.items():
            color = int(color_coord[0][-1])
            coords = color_coord[1]
            for coord in coords:
                self.drawer.point(coord, self.shoe_color[color])
