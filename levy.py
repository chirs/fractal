
import math
import time
import itertools

# Abstract implementation of Levy C curve - a fractal.


def get_midpoint(a, b):
    return (a[0] + b[0]) / 2.0, (a[1] + b[1]) / 2.0

def get_distance(a, b):
    return math.sqrt((a[0]-b[0])**2 + (a[1]-b[1])**2)


def koch_curve(steps=0):
    # A standard triangular koch curve.

    def step(s):
        s2 = ''
        for c in s:
            if c == 'a':
                s2 += 'arallara'
            else:
                s2 += c

        return s2

        

    s = 'allalla'
    
    i = 0
    while True:
        if i == steps:
            return s

        s = step(s)
        i += 1

def sierpinski_triangle_string(steps=0):
    def step(s):
        s2 = ''
        for c in s:
            if c == 'a':
                s2 += 'b-a-b'
            elif c == 'b':
                s2 += 'a+b+a'
            else:
                s2 += c

        return s2

    s = 'a'
    i = 0
    while True:
        if i == steps:
            return s

        s = step(s)
        i += 1
                


def generate_levy_c_curve_grammar(steps=0):
    
    def process_string(s):
        s2 = ''
        for char in s:
            if char == 'f':
                s2 += '+f--f+'
            else:
                s2 += char

        return s2

    s = 'f'
    i = 0
    while True:
        if steps == i:
            return s
        
        i += 1
        s = process_string(s)

    
    

def cantor_dust_alphabet(steps=0):


    def dust_step(s):
        s2 = ''
        for char in s:
            if char == 'a':
                s2 += 'aba'
            elif char == 'b':
                s2 += 'bbb'
            else:
                import pdb; pdb.set_trace()
        return s2

    s = 'a'
    i = 0
    while True:
        if steps == i:
            return s

        i += 1
        s = dust_step(s)




def sierpinski_number(i):
    for ix, e in enumerate(sierpinski()):
        if i == ix: 
            return e

def sierpinski():
    a, b, c =(0, 0), (1, 0), (.5, math.sqrt(3) / math.sqrt(2))
    triangles = [(a,b,c)]

    i = 0

    for e in itertools.count():
        #time.sleep(5)
        tx = []
        for t in triangles:
            tx.extend(sierpinski_dissect(t))

        triangles = tx
        yield triangles



def sierpinski_dissect(points):
    a, b, c = points
    abm, bcm, cam = [get_midpoint(*e) for e in [(a,b), (b,c), (c,a)]]
    return [
        (a, abm, cam),
        (b, bcm, abm),
        (c, bcm, cam),
        ]
    







        
def levy():
    points = (a, b)
    while True:
        points = levy_step(points)
    
    

def levy_step(points):

    def find_levy_midpoint(a, b):
        # create a 45, 45, 90 triangle endpoint facing the correct direction.

        midpoint = get_midpoint(a, b)
        length = get_distance(a, midpoint)

        if a[0] < b[0] and a[1] < b[1]:
            np = (a[0] + length, a[1])
        elif a[0] < b[0] and a[1] == b[1]:
            np = (a[0] + b[0])


        new_midpoint = some_math()
        return new_midpoint


    new_points = []

    paired_points = zip(points, points[1:])
    
    new_points.append(paired_points[0][0])
    for a, b in paired_points:
        midpoint = find_levy_midpoint(a, b)
        new_points.append(midpoint)
        new_points.append(b)

    return new_points



    
    
        
if __name__ == "__main__":
    print koch_curve(2)
    #print koch_curve(10)
    #for e in sierpinski():
    #    print e
        
        
    
