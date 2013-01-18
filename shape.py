



# Old drawing methods.
"""
from lsystem import sierpinski
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
"""


"""
# Separate?

def sierpinski_old():
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
    # Given three points, cut into four triangles a la Sierpinski's triangle
    a, b, c = points
    abm, bcm, cam = [get_midpoint(*e) for e in [(a,b), (b,c), (c,a)]]
    return [
        (a, abm, cam),
        (b, bcm, abm),
        (c, bcm, cam),
        ]
    
# Original levy generation method.
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


"""
    
