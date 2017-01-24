
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

hilbert = Lsystem('a', hilbert_mapping)

koch = Lsystem('allalla', {'a': 'arallara'})



sierpinski_mapping = {
    'a': 'b-a-b',
    'b': 'a+b+a',
    }

sierpinski = Lsystem('a', sierpinski_mapping)


binary_mapping = {
    '1': '11',
    '0': '1[0]0',
    }

binary = Lsystem('0', binary_mapping)




cantor_dust_mapping = {
    'a': 'aba',
    'b': 'bbb',
    }

cantor = Lsystem('a', cantor_dust_mapping)

levy_mapping = { 'f': '+f--f+', }

levy = Lsystem('f', levy_mapping)


### Old code

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
    #print(hilbert2.generate(5))

    print(levy_mapping)

    print('\n1: ' + levy.generate(1))
    print('\n4: ' + levy.generate(4))              
    print('\n7: ' + levy.generate(7))
    print('\n10: ' + levy.generate(10))            

    #print(levy.generate(13))
