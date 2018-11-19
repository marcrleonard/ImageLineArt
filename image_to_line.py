import svgwrite
from svgwrite.container import Group
from svgwrite import path as spath
from svgwrite.shapes import Polyline, Polygon, Rect

import numpy as np

from PIL import Image
imag = Image.open("/Users/marcleonard/Desktop/me_lg_w.png")
#Convert the image te RGB if it is a .gif for example
imag = imag.convert ('RGB')

width, height = imag.size

imag.thumbnail((width*.6, height*.6), Image.ANTIALIAS)
width, height = imag.size
print('width: {}'.format(width))
print('height: {}'.format(height))




yo = Image.open("/Users/marcleonard/Desktop/me_lg_w.png").convert('L')

all_pixels = np.array(yo) # im2arr.shape: height x width x channel
# arr2im = Image.fromarray(im2arr)


# all_pixels = []
# for col in range(width):
#     row = []
#     for pixel in range(height):
#         pixelRGB = imag.getpixel((col,pixel))
#         R,G,B = pixelRGB
#         brightness = int(sum([R,G,B])/3)
#         row.append(brightness)
#
#     all_pixels.append(row)
#
# print(all_pixels)


dwg = svgwrite.Drawing('asd.svg',
                       # size=('{}px'.format(width), '{}px'.format(height))
                       size=('420mm', '297mm'),
                        viewBox=('0 0 {} {}'.format(1190*2,841.9*2 ))
                       )


rect = Rect(insert=(0,0), size=('100%', '100%'),
            stroke='black',
            fill_opacity=0,
            )

dwg.add(rect)

g = dwg.add(Group())



low_clip = .15
high_clip = .65

spacing = 9
# spacing = 6
circle_size = .05

num_line=0

scale = .18

prev_x = 0
prev_y = 0



# for (x, y), pixel in np.ndenumerate(all_pixels):
#
#     if (y % spacing == 0):
#
#
#         obj = spath.Path(stroke=svgwrite.rgb(10, 10, 16, '%'))
#
#         # obj_add = Polyline([(0, y)], stroke=svgwrite.rgb(10, 10, 16, '%'), fill_opacity=0)
#
#         s1 = 'M {} {}'.format(0, y)
#         p3 = dwg.path(d=s1, stroke_width=1, stroke='black', fill='none')
#         # top left to top right
#
#         l1l = []
#
#         add = False
#
#         if (x % spacing  == 0 ):
#             add = True
#
#             pixel = (pixel - 255) * -1 * scale
#
#             l1l.append(x)
#             l1l.append(y - pixel)
#
#             p3.push('L', l1l)
#
#         if add:
#             dwg.add(p3)
#



for y, row in enumerate(all_pixels):
    if (y % spacing == 0):

        d = ''


        obj = spath.Path(stroke=svgwrite.rgb(10, 10, 16, '%'))

        # obj_add = Polyline([(0, y)], stroke=svgwrite.rgb(10, 10, 16, '%'), fill_opacity=0)

        s1 = 'M {} {}'.format(0, y)
        p3 = dwg.path(d=s1, stroke_width=1, stroke='black', fill='none')
        # top left to top right

        l1l = []
        for x, pixel in enumerate(row):

            if (x % spacing  == 0 ):

                pixel = (pixel - 255) * -1 * scale

                l1l.append(x)
                l1l.append(y - pixel)


        p3.push('L', l1l)
        num_line += 1

        g.add(p3)


print(num_line)
dwg.saveas('asd_poly.svg', pretty=True)


