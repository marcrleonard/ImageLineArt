import svgwrite
from svgwrite import path as spath
from svgwrite.shapes import Polyline


input_list = [
    [1,0,0,0,0,0,0,1],
    [1,0,0,10,10,0,0,1],
    [1,0,0,0,0,0,0,1]
]
spacing = 20


dwg = svgwrite.Drawing('asd.svg',
                       # size=('{}px'.format(width), '{}px'.format(height))
                       size=('420mm', '297mm'),
                        # viewBox=('0 0 420 297')

                       )


for y, row in enumerate(input_list):
        for x, value in enumerate(row):


            if value > 0:
                obj_add = dwg.circle(
                    center=(x+spacing,y+spacing),
                    r=value,
                    stroke='black',
                    fill_opacity=0,
                )
                dwg.add(obj_add)



dwg.saveas('compare_1.svg', pretty=True)