#from pyprocessing import *
import random
from levy import sierpinski, sierpinski_number, generate_levy_c_curve_grammar, koch_curve, sierpinski_triangle_string
import math

#import svgwrite


import pysvg.structure
import pysvg.builders
import pysvg.text




XSIZE = 800
YSIZE = 800


def setup():
    size(XSIZE, YSIZE)
    frameRate(1)
    background(255)


class Turtle(object):

    def __init__(self):
        self.coordinates = (0, 0)
        self.degrees = 0
        self.orientation = math.pi

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


    def __init__(self, fn):
        super(SVGTurtle, self).__init__()
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




def draw_sierpinski():
    for triangles in sierpinski():
        #if random.random() > .75:
        if random.random() > .1:
            return
        
        print triangles
        time.sleep(2)
        background(255)
        for a,b,c in triangles:
            draw_triangle(a,b,c)


def draw_triangle(a,b,c):
    print "drawing"
    for (p1, p2) in [(a,b), (a,c), (b,c)]:
        x1, y1 = [XSIZE * e for e in p1]
        x2, y2 = [YSIZE * e for e in p2]
        print x1, y1, x2, y2
        line(x1, y1, x2, y2)


def draw_sierpinski_points(triangles):
    for a,b,c in triangles:
        draw_triangle(a,b,c)


def process_levy_string(s, turtle):
    for char in s:
        if char == '+': 
            turtle.right(45)
        elif char == '-':
            turtle.left(45)
        elif char == 'f':
            turtle.forward(5)
        else:
            import pdb; pdb.set_trace()




def read_cantor(s, a, b):
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
            
                            


def draw():
    #background(255)
    #draw_line(0, YSIZE/2)
    #px = sierpinski_number(9)
    #draw_sierpinski_points(px)
    #line(0, 0, 500, 500)

    t = SVGTurtle('sierpinski.svg')

    #t.right(150)
    #t.forward(300, draw=False)
    #kc = koch_curve(steps=8)
    #process_koch_string(kc, t, step=.02)

    t.right(140)
    t.forward(400, draw=False)

    sts = sierpinski_triangle_string(steps=5)
    #print sts
    process_sierpinski_string(sts, t, step=1)

    t.save()

    #steps = random.choice(range(0, 15))
    #print steps
    #s = generate_levy_c_curve_grammar(steps=steps)
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

