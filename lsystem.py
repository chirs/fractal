
import math
import time
import itertools

# Working implementation Lindenmayer system fractals - generated using a rewriting system, which include
# Levy C Curve, Koch Curve, Sierpinski Triangle, Cantos Dust; also model biological systems particularly well.


class Lsystem(object):
    def __init__(self, start, rules):
        self.start = start
        self.rules = rules

    def rewrite(self, s):
        s_ = ''
        for char in s:
            s_ += self.rules.get(char, char)
        return s_


    def generate(self, depth=1):
        s = self.start
        for e in range(depth):
            #import pdb; pdb.set_trace()
            s = self.rewrite(s)

            
        return s

hilbert_mapping = {
    'a': '-bf+afa+fb-',
    'b': '+af-bfb-fa+',
}

hilbert2 = Lsystem('a', hilbert_mapping)

koch2 = Lsystem('allalla', {'a': 'arallara'})
            

def generic_lsystem(start, fn):
    """
    Generate arbitrarily long l systems.
    """
    s = start
    for e in itertools.count():
        yield s
        s = fn(s)


def lsx(generator, depth):
    """
    Extract a string from lsystem generator.
    """

    for e in range(depth):
        x = generator.next()
    return x


def koch_curve2():
    
    def step(s):
        mapping = {
            'a': 'arallara',
            }
        
        s2 = ''
        for c in s:
            if c == 'a':
                s2 += 'arallara'
            else:
                s2 += c

        return s2

    return generic_lsystem('allalla', step)


def hilbert():
    
    def step(s):
        mapping = {
            'a': '-bf+afa+fb-',
            'b': '+af-bfb-fa+',
            }

        s2 = ''
        for c in s:
            s2 += mapping.get(c, c)
        return s2

    return generic_lsystem('a', step)


def sierpinski2():
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

    return generic_lsystem('a', step)


def binary_tree(steps=0):
    
    def process_string(s):
        s2 = ''
        for char in s:
            if char == '1':
                s2 += '11'
            elif char == '0':
                s2 += '1[0]0'
            else:
                s2 += char

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
    #print(binary_tree(8))
    #print(lsx(koch_curve2(), 5))
    print(hilbert2.generate(5))
        
    
