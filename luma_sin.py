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

import datetime

t1 = datetime.datetime.utcnow()

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

# g = dwg.add()
g = Group()



low_clip = .15
high_clip = .65

x_spacing = 10
y_spacing = 15

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

# x:input value;
# a,b:input range
# c,d:output range
# y:return value
# Function:
def mapFromTo(x,a,b,c,d):
   y=(x-a)/(b-a)*(d-c)+c
   return y



for y, row in enumerate(all_pixels):
    if (y % y_spacing == 0):

        d = ''


        # obj = spath.Path(stroke=svgwrite.rgb(10, 10, 16, '%'))

        obj = Polyline(points=[(0, y)],
                       stroke=svgwrite.rgb(10, 10, 16, '%'),
                       fill_opacity=0,
                       # fill='white'
                       debug=False
                       )
        # obj.debug = False


        # s1 = 'M {} {}'.format(0, y)
        # p3 = dwg.path(d=s1, stroke_width=1, stroke='black', fill='none')
        # top left to top right

        l1l = []
        for x, pixel in enumerate(row):

            if (x % x_spacing  == 0 ):

                o_v = (pixel - 255) * -1    # * scale

                value = mapFromTo(o_v, 0,255,0,10)

                add_line = True

                if o_v > 10:
                    add_line = False


                    Fs = x_spacing  # sample rate
                    f = value  # frequency
                    sample = x_spacing
                    x_list = np.arange(sample)
                    y_list = np.sin(2 * np.pi * f * x_list / Fs)


                    # spikes = int(x_spacing/3)
                    # print('spikes '+ str(spikes))

                    _spacing = int(x_spacing/2)

                    for s in range(_spacing):

                        a = 10

                        _x = x_list[s]
                        _y = y_list[s]
                                                    # adding this spacing
                                                    # puts it in the middle-ish
                        obj.points.append((x + _x + (_spacing/2), y + (_y* a)))
                #     print('{} -> {}'.format(o_v, value))

                if add_line:
                    obj.points.append((x, y))

        num_line += 1

        g.add(obj)


print(num_line)
dwg.add(g)
dwg.saveas('luma_sin.svg', pretty=True)

t2 = datetime.datetime.utcnow()

t = str((t2-t1).total_seconds())  + ' micro seconds'

print(t)

print('file:///Users/marcleonard/Projects/ImageLineArt/luma_sin.svg')

#  0.6258882666666667 minutes

