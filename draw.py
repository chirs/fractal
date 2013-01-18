
#from pyprocessing import *
import random
from lsystem import generate_levy_c_curve_grammar, koch_curve_string, sierpinski_triangle_string
import math

#import svgwrite
import pysvg.structure
import pysvg.builders
import pysvg.text


# Machinery for actually drawing images.

"""
XSIZE = 800
YSIZE = 800

def setup():
    size(XSIZE, YSIZE)
    frameRate(1)
    background(255)
"""

# Use pysvg Turtle object instead?
class Turtle(object):
    # A classic logo-style turtle.
    # Response to forward(10, draw=True) and right/left(45)

    def __init__(self, coordinates=None, degrees=None):
        if self.coordinates is None:
            self.coordinates = (0, 0)
        else:
            self.coordinates = coordinates

        if self.degrees is None: 
            self.degrees = 0
            self.orientation = math.pi

        else:
            self.degrees = degrees
            self.orientation = math.pi - (degrees * math.pi / 180)


    def left(self, degrees):
        self.degrees += degrees
        
        radians = (degrees * math.pi) / 180
        self.orientation = self.orientation + radians

    def right(self, degrees):
        self.left(-degrees)

    def forward(self, distance, draw=True):
        xd = math.cos(self.orientation) * distance
        yd = math.sin(self.orientation) * distance
        x0, y0 = self.coordinates
        x1, y1 = x0 + xd, y0 + yd
        self.coordinates = (x1, y1)

        if draw:
            self.draw_line((x0, y0), (x1, y1))
            #line(x0, y0, x1, y1)

    
    def draw_line(self, p0, p1):
        line(p0[0], p0[1], p1[0], p1[1])


    def save(self):
        pass


class SVGTurtle(Turtle):

    # A turtle that creates an svg. Currently only creates lines.
    # Have to call save().


    def __init__(self, fn=None, drawing=None):
        super(SVGTurtle, self).__init__()
        
        assert fn or drawing
        #self.drawing = svgwrite.Drawing(fn, profile='tiny')

        self.drawing = pysvg.structure.Svg()

        self._fn = fn
        self._builder = pysvg.builders.ShapeBuilder()

    def save(self):
        #self.drawing.save()
        self.drawing.save(self._fn)
        

    def draw_line(self, p0, p1):
        #self.drawing.add(self.drawing.line(p0, p1, stroke=svgwrite.rgb(255, 0, 0, '%')))
        self.drawing.addElement(self._builder.createLine(p0[0], p0[1], p1[0], p1[1], strokewidth=1, stroke='black'))



# Alphabet processing functions.

def process_levy_string(s, turtle):

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
    distance = get_distance(a, b)
    step_length = len(s) / float(distance)
    lines = []
    for i, char in enumerate(s):
        x0 = step_legth * i
        if char == 'a':
            lines.append(((0, x0), (0, x0 + step_length)))

    for line in lines:
        draw_line(line)


def process_koch_string(s, turtle, step=5):
    for char in s:
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
        elif char == ']':
            turtles.pop()
            turtle = turtles[-1]

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


    #t.right(150)
    #t.forward(300, draw=False)
    #kc = koch_curve_string(steps=8)
    #process_koch_string(kc, t, step=.02)

    #t.right(140)
    #t.forward(400, draw=False)

    #sts = sierpinski_triangle_string(steps=5)
    #print sts
    #process_sierpinski_string(sts, t, step=1)

    #t.save()

    t = SVGTurtle('levy.svg')
    #steps = random.choice(range(0, 15))
    #print steps

    t.right(150)
    t.forward(550, draw=False)
    t.left(150)
    

    s = generate_levy_c_curve_grammar(steps=16)
    process_levy_string(s, t)
    t.save()
    
    #process_levy_string(s, t)
    #t.right(30)
    #t.forward(200)
    #t.right(90)
    #t.forward(200)

    #fn = "images/trees/%s.png" % str(random.random())[2:]
    #get().save(fn)

#run()





if __name__ == "__main__":
    draw()

