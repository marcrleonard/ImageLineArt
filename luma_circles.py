import svgwrite
from svgwrite import path as spath

from svgwrite.container import Group
from svgwrite.shapes import Polyline, Rect

from PIL import Image

import numpy as np

imag = Image.open("/Users/marcleonard/Desktop/me_lg_w_2 copy.png")
#Convert the image te RGB if it is a .gif for example
imag = imag.convert ('RGB')

width, height = imag.size

imag.thumbnail((width*.6, height*.6), Image.ANTIALIAS)
width, height = imag.size
print('width: {}'.format(width))
print('height: {}'.format(height))


# yo = Image.open("/Users/marcleonard/Desktop/me_lg_w.png").convert('L')
# all_pixels = np.array(yo)

all_pixels = []

for col in range(width):
    row = []
    for pixel in range(height):
        pixelRGB = imag.getpixel((col,pixel))
        R,G,B = pixelRGB
        brightness = int(sum([R,G,B])/3)
        row.append(brightness)

    all_pixels.append(row)

print(all_pixels)

# 297 x 420


# <rect fill="#FF5B00" height="1184" stroke="#000000" width="768" x="0" y="0"/>


dwg = svgwrite.Drawing('asd.svg',
                       # size=('{}px'.format(width), '{}px'.format(height))
                       size=('420mm', '297mm'),
                        viewBox=('0 0 1190 841.9')
                       )


low_clip = .55
high_clip = .15

spacing = 9
circle_size = .05

obj=0

rect = Rect(insert=(0,0), size=('100%', '100%'),
            stroke='black',
            fill_opacity=0,
            )

dwg.add(rect)

g = dwg.add(Group())

flip = False
if flip:
    all_pixels = all_pixels[::-1]

for y, row in enumerate(all_pixels):
    if (y % spacing == 0):

        for x, value in enumerate(row):

            if (x % spacing  == 0 ):



                organic_x = True
                o_x = 0
                if organic_x:
                    import random

                    o_x = random.uniform(-1.5, 1.5)


                value = ( value - 255) * -1
                size = value*circle_size

                obj_add = None

                if size > high_clip:
                    obj_add = Polyline([(y, x + o_x),(y, x + 1 + o_x)],
                                       stroke='black',
                                       fill_opacity=0,
                                       )

                if size > low_clip:
                    obj_add = dwg.circle(center=(y, x + o_x),
                                         r=size,
                                         stroke='black',
                                         fill_opacity=0,
                                         )


                if obj_add:
                    g.add(obj_add)
                    obj += 1



print(obj)

# dwg.add(g)

dwg.saveas('marc_circles.svg', pretty=True)
