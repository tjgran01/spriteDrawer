import os
from PIL import Image


class SpriteParser(object):
    def __init__(self, im):
        self.im = Image.open(im)
        self.colors, self.all_col_coords = self.get_pixel_coords()
        self.color_amt = len(self.colors)
        self.dict_title = im[im.rfind("/") + 1:-4]

        self.write_coords_to_dict()


    def get_pixel_coords(self):

        pixels = [data for i, data in enumerate(self.im.getdata())
                  if data != (255, 255, 255, 255)]
        colors = []

        for pixel in pixels:
            if pixel not in colors:
                colors.append(pixel)

        all_col_coords = {}
        for i_0, color in enumerate(colors):
            col_coords = {f"color_{i_0}": []}
            for i_1, pixel in enumerate(self.im.getdata()):
                coord = divmod(i_1, self.im.width)
                if pixel == color:
                    col_coords[f"color_{i_0}"].append((coord[1], coord[0]))
            all_col_coords.update(col_coords)

        return (colors, all_col_coords)


    def write_coords_to_dict(self):

        with open("./coord_dicts.py", "a") as out_file:
            out_file.write(f"'{self.dict_title}': {self.all_col_coords}")


fpath = f"{os.getcwd()}/../originals/overalls_1.png"

s = SpriteParser(fpath)
print(s.colors)
print(s.dict_title)
