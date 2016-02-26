#!/usr/bin/env python

import random
import math

#import pysvg.structure
#import pysvg.builders
#import pysvg.text
#from pyprocessing import *
#import svgwrite

from lsystem import ultra, generate_levy_c_curve_grammar, koch_curve2, sierpinski2, binary_tree


# Machinery for actually drawing images.
# Includes an Abstract Turtle, an SVG turtle, ...
# needs to handle three dimensions

"""
XSIZE = 800
YSIZE = 800

def setup():
    size(XSIZE, YSIZE)
    frameRate(1)
    background(255)
"""


class Turtle(object):
    """
    A classic logo-style turtle.
    Response to forward(10, draw=True) and right/left(45)
    """
    # Use pysvg Turtle object instead?

    def __init__(self, coordinates=None, degrees=None):
        if coordinates is None:
            self.coordinates = (0, 0, 0)
        else:
            self.coordinates = coordinates

        # Turn degrees into a property.
        if degrees is None: 
            self.degrees = 0
            self.orientation = math.pi

        else:
            self.degrees = degrees
            self.orientation = math.pi - (degrees * math.pi / 180)

        self.pen = True


    def copy(self):
        return Turtle(self.coordinates, self.degrees)


    def left(self, degrees):
        self.degrees += degrees
        
        radians = (degrees * math.pi) / 180
        self.orientation = self.orientation + radians

    def right(self, degrees):
        self.left(-degrees)

    def forward(self, distance):
        xd = math.cos(self.orientation) * distance
        yd = math.sin(self.orientation) * distance
        x0, y0, _ = self.coordinates
        x1, y1 = x0 + xd, y0 + yd
        self.coordinates = (x1, y1, 0)

        if self.pen:
            self.draw_line((x0, y0, 0), (x1, y1, 0))
            #line(x0, y0, x1, y1)

    def draw_line(self, p0, p1):
        #line(p0[0], p0[1], p1[0], p1[1])
        raise

    def up(self):
        self.pen = False

    def down(self):
        self.pen = True

    def save(self):
        pass


class RhinoTurtle(Turtle):
    """
    A Turtle that works with Rhino.
    """

    def __init__(self, coordinates=None, degrees=None):
        super(RhinoTurtle, self).__init__()

    def draw_line(self, p0, p1):
        import rhinoscriptsyntax as rs
        rs.AddLine(p0, p1)

    


class SVGTurtle(Turtle):
    """
    A turtle that creates an svg. Currently only creates lines.
    Have to call save().
    """


    def __init__(self, coordinates=None, degrees=None, fn=None, drawing=None):
        super(SVGTurtle, self).__init__()
        
        assert fn or drawing # file or drawing object
        #self.drawing = svgwrite.Drawing(fn, profile='tiny')

        if drawing:
            self.drawing = drawing
        else:
            self.drawing = pysvg.structure.Svg()

        self._fn = fn
        self._builder = pysvg.builders.ShapeBuilder()


    def copy(self):
        return SVGTurtle(self.coordinates, self.degrees, fn=self._fn, drawing=self.drawing)
        

    def save(self):
        #self.drawing.save()
        self.drawing.save(self._fn)
        

    def draw_line(self, p0, p1):
        #self.drawing.add(self.drawing.line(p0, p1, stroke=svgwrite.rgb(255, 0, 0, '%')))
        self.drawing.addElement(self._builder.createLine(p0[0], p0[1], p1[0], p1[1], strokewidth=1, stroke='black'))



# Alphabet processing functions.

def process_levy_string(s, turtle):
    """
    Transform a levy string encoding into a drawing.
    """

    distance = 30 * (1 / math.log(len(s), 2))

    for char in s:
        if char == '+': 
            turtle.right(45)
        elif char == '-':
            turtle.left(45)
        elif char == 'f':
            turtle.forward(distance)
        else:
            import pdb; pdb.set_trace()


def process_cantor_string(s, a, b):
    """
    Transform cantor string encoding to form.
    """
    distance = get_distance(a, b)
    step_length = len(s) / float(distance)
    lines = []
    for i, char in enumerate(s):
        x0 = step_legth * i
        if char == 'a':
            lines.append(((0, x0), (0, x0 + step_length)))

    for line in lines:
        draw_line(line)


def process_koch_string(turtle, string, step=5):
    for char in string:
        if char == 'l':
            turtle.left(60)
        elif char == 'r':
            turtle.right(60)
        else:
            turtle.forward(step)


def process_sierpinski_string(s, turtle, step=5):
    for char in s:
        if char == '+':
            turtle.left(60)
        elif char == '-':
            turtle.right(60)
        else:
            turtle.forward(step)



def process_binary(s, turtle):
    turtles = [turtle]
    for char in s: 
        if char == '[':
            t = turtle.copy()
            turtles.append(t)

            turtle = t
            turtle.left(45)

        elif char == ']':
            turtles.pop()

            turtle = turtles[-1]
            turtle.right(45)

        elif char in '01':
            turtle.forward(5)

        else:
            import pdb; pdb.set_trace()
                            


def draw():
    #background(255)
    #draw_line(0, YSIZE/2)
    #px = sierpinski_number(9)
    #draw_sierpinski_points(px)
    #line(0, 0, 500, 500)

    #t = SVGTurtle('sierpinski.svg')



    """
    t.right(150)
    t.up()
    t.forward(300)
    t.down()

    """

    t = RhinoTurtle()
    #s = lsystem_string(koch_curve2(), 5)
    s = lsystem_string(koch_curve2(), 5)
    process_koch_string(t, s, step=1)

    """

    #t.right(140)
    #t.forward(400, draw=False)

    #sts = sierpinski_triangle_string(steps=5)
    #print sts
    #process_sierpinski_string(sts, t, step=1)

    #t.save()


    #steps = random.choice(range(0, 15))
    #print steps


    t = SVGTurtle(fn='binary.svg')
    t.right(150)
    t.forward(550, draw=False)
    t.left(150)
    #s = generate_levy_c_curve_grammar(steps=16)
    s = binary_tree(steps=7)
    print s
    process_binary(s, t)
    t.save()

    
    #process_levy_string(s, t)
    #t.right(30)
    #t.forward(200)
    #t.right(90)
    #t.forward(200)

    #fn = "images/trees/%s.png" % str(random.random())[2:]
    #get().save(fn)
    """

#run()





if __name__ == "__main__":
    draw()

