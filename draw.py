
import random
import math

from lsystem import hilbert, koch, sierpinski, binary, cantor, levy, plant, stoch1


class Turtle(object):
    """
    A classic logo-style turtle.
    Response to forward(10, draw=True) and right/left(45)
    """


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

    # pitch, yaw, roll

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
        super(RhinoTurtle, self).__init__(coordinates, degrees)

    def draw_line(self, p0, p1):
        import rhinoscriptsyntax as rs
        rs.AddLine(p0, p1)
        pass


    def copy(self):
        # fix this... use __super__ ??
        return RhinoTurtle(self.coordinates, self.degrees)


class Turtle3d(object):

    def __init__(self, position=None, orientation=None):
        
        if position is None:
            position = (0, 0, 0)

        # Heading, left, up.
        if orientation is None:
            orientation = [
                (1, 0, 0),
                (0, 1, 0),
                (0, 0, 1)
                ]

        self.position = position
        self.orientation = orientation


    # Orientation vectors
    def orientation_vector(self, index, value=None):
        if value is not None:
            self.orientation[index] = value
            return None
        else:
            return self.orientation[index]

    def heading(self, value=None):
        return self.orientation_vector(0, value)

    def left(self, value=None):
        return self.orientation_vector(1, value)

    def up(self, value=None):
        return self.orientation_vector(2, value)

    def yaw(self, radians):
        h_ = self.heading()
        nh_ = [-1 * e for e in h_]
        l_ = self.left()
        self.left(rotate(l_, nh_, radians))
        self.heading(rotate(h_, l_, radians))

    def pitch(self, radians):
        h_ = self.heading()
        nh_ = [-1 * e for e in h_]
        u_ = self.up()
        self.up(rotate(u_, nh_, radians))
        self.heading(rotate(h_, u_, radians))

    def roll(self, radians):
        l_ = self.left()
        nl_ = [1 * e for e in l_]
        u_ = self.up()
        self.up(rotate(u_, nl_, radians))
        self.left(rotate(l_, u_, radians))


    def draw_line(self, p0, p1):
        import rhinoscriptsyntax as rs
        rs.AddLine(p0, p1)
    

    def forward(self, distance):

        hv = [distance * s for s in  self.heading()]

        p0 = self.position
        self.position = [a + b for (a, b) in zip(hv, p0)]

        if True:
            self.draw_line(p0, self.position)
        


def rotate(v1, v2, radians):
    """
    rotate around perpindicular vectors v1 and v2
    """
    # assert dot_product(v1, v2) == 0

    
    # how to ensure v1 and v2 are perpindicular?
    # (are any two vectors by their nature perpindicular? (no??)
    # seriously? This is all? Let's see.
    return [math.cos(radians) * s1 + math.sin(radians) * s2 for (s1, s2) in zip(v1, v2)]

    
    
    
# Alphabet processing functions.

def process_levy(turtle, string):
    """
    Transform a levy string encoding into a drawing.
    """

    distance = 30 * (1 / math.log(len(string), 2))

    for char in string:
        if char == '+': 
            turtle.right(45)
        elif char == '-':
            turtle.left(45)
        elif char == 'f':
            turtle.forward(distance)
        else:
            import pdb; pdb.set_trace()


def process_cantor(s, a, b):
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


def process_koch(turtle, string, step=5):
    for char in string:
        if char == 'l':
            turtle.left(60)
        elif char == 'r':
            turtle.right(60)
        else:
            turtle.forward(step)

            
def process_hilbert(turtle, string, step=1):
    for char in string:
        if char == '-':
            turtle.left(90)
        elif char == '+':
            turtle.right(90)
        elif char == 'f':
            turtle.forward(step)
        

def process_sierpinski(turtle, string, step=5):
    for char in string:
        if char == '+':
            turtle.left(60)
        elif char == '-':
            turtle.right(60)
        else:
            turtle.forward(step)


def process_binary(turtle, string):
    turtles = [turtle]

    for char in string: 
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


def draw_hilbert3d(string):

    return draw_generic(Turtle3d(), {
        '&': lambda t: t.forward(10),
         '+': lambda t: t.right(45),
         '-': lambda t: t.left(45),
         '.': lambda t: t.yaw(45),
         'A': lambda t: t.yaw(45),
         'B': lambda t: t.yaw(45),
         'C': lambda t: t.yaw(45),
         'D': lambda t: t.yaw(45),
         'F': lambda t: t.yaw(45),
         '|': lambda t: t.yaw(45),
         })


def draw_generic(turtle, mapping, string):


    funcs = [mapping[char] for char in string if char in mapping]
    for f in funcs:
        f(turtle)
        
    """
    for char in string:
        if char in mapping:
            func = mapping[char]
            func(turtle)
    """

    return turtle


def draw_stochastic(s):

    return draw_generic(RhinoTurtle(), {
        'a': lambda t: t.forward(10),
        'b': lambda t: t.right(90),
        'c': lambda t: t.left(90),        
         }, s)
    
    
                            


def process_plant(turtle, string):
    turtle_stack = []
    current_turtle = turtle
    
    
    for char in string:
        if char == 'f':
            current_turtle.forward(5)
        elif char == '-':
            current_turtle.left(25)
        elif char == '+':
            current_turtle.right(25)
        elif char == '[':

            tu = current_turtle.copy()
            turtle_stack.append(current_turtle)
            current_turtle = tu
        elif char == ']':

            current_turtle = turtle_stack.pop()
            pass
            

def process_sl(turtle, string):

    for char in string:
        if char == 'a':
            turtle.forward(10)
        elif char == '+':
            turtle.left(60)
        elif char == '-':
            turtle.right(60)
        else:
            pass







def main():

    #test_turtle3d()
    
    #turtle = RhinoTurtle()

    #process_sl(turtle, sl.generate(12))

    draw_stochastic(stoch1.generate(9))


    #process_plant(turtle, plant.generate(7))

    #process_sierpinski(turtle, sierpinski.generate(7))
    #process_levy(turtle, levy.generate(13))    
    #process_koch(turtle, koch.generate(7))
    #process_hilbert(turtle, hilbert.generate(7))




def test_turtle3d():

    t = Turtle3d()
    t.forward(10)
    t.pitch(.25 * math.pi)
    t.forward(10)
    t.roll(math.pi)
    t.forward(10)
    t.pitch(.25 * math.pi)
    t.forward(10)
    t.yaw(.55 * math.pi)
    t.forward(10)


if __name__ == "__main__":
    main()

            
            
