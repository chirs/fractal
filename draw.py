
import random
import math

from lsystem import generate_levy_c_curve_grammar, lsx

from lsystem import hilbert, koch, sierpinski, binary, cantor, levy, plant


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
            



def main():
    turtle = RhinoTurtle()

    process_plant(turtle, plant.generate(7))

    #process_sierpinski(turtle, sierpinski.generate(7))
    #process_levy(turtle, levy.generate(13))    
    #process_koch(turtle, koch.generate(7))
    #process_hilbert(turtle, hilbert.generate(7))






if __name__ == "__main__":
    main()

            
            
