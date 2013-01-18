
import math
import time
import itertools

# Working implementation Lindenmayer system fractals - generated using a rewriting system, which include
# Levy C Curve, Koch Curve, Sierpinski Triangle, Cantos Dust; also model biological systems particularly well.


def get_midpoint(a, b):
    return (a[0] + b[0]) / 2.0, (a[1] + b[1]) / 2.0

def get_distance(a, b):
    return math.sqrt((a[0]-b[0])**2 + (a[1]-b[1])**2)


def koch_curve_string(steps=0):
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
    # Sierpinski Triangle

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


def binary_tree(steps=0):
    
    def process_string(s):
        s2 = ''
        for char in s:
            if char == '1':
                s2 += '11'
            elif char == '0':
                s2 += '1[0]0'
            else:
                s2 += 'char'

        return s2

    s = '0'
    i = 0
    while True:
        if steps == i:
            return s
        
        i += 1
        s = process_string(s)
                


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

    
    

def cantor_dust_string(steps=0):

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


if __name__ == "__main__":
    pass
        
    
