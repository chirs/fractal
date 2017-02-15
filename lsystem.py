

import itertools
import math
import random
import time


# Working implementation Lindenmayer system fractals - generated using a rewriting system, which include
# Levy C Curve, Koch Curve, Sierpinski Triangle, Cantos Dust; also model biological systems particularly well.

"""
Variations:

1. Stochastic grammers: 0 (.5) -> 1[0]0; 0 (.5) -> 0
2. Context sensitive grammars: b < a > c ->  aa
transforms "a" to "aa", but only If the "a" occurs between a "b" and a "c" in the input string:
3. Parametric grammars: not as interesting to me.

Focus on stochastic grammars
"""


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
            s = self.rewrite(s)
            
        return s

    def alphabet(self):
        chars = set(self.rules.keys())
        for v in self.rules.values():
            for c in v:
                chars.add(c)
        return sorted(chars)


class Stochastic(Lsystem):

    def rewrite(self, s):

        def subroutine(probability_list):
            r = random.random()
            s = 0
            for (probability, string) in probability_list:
                s += probability
                if r < s:
                    return string

            import pdb; pdb.set_trace()

            return string
        
        s_ = ''
        if s is None:
            import pdb; pdb.set_trace()
            
        for char in s:
            v = self.rules.get(char)

            if v is None:
                # s_ += char 
                pass # ignore if not in alphabet
            elif type(v) == type('a'): # bad python?
                s_ += v
            elif type(v) == type([]):
                s_ += subroutine(v)

        return s_


stoch1 = Stochastic('a', {
    'a': [(.5, 'aa'), (.5, 'abca')],
    'b': [(.25, 'bb'), (.75, 'aca')],
    'c': [(.25, 'ccc'), (.75, 'abba')],
    })
            
        

hilbert = Lsystem('a', {
    'a': '-bf+afa+fb-',
    'b': '+af-bfb-fa+',
})

koch = Lsystem('allalla', {'a': 'arallara'})


plant = Lsystem('x', {
    'x': 'f-[[x]+x]+f[+fx]-x',
    'f': 'ff',
    })

sierpinski = Lsystem('a', {
    'a': 'b-a-b',
    'b': 'a+b+a',
    })


binary = Lsystem('0', {
    '1': '11',
    '0': '1[0]0',
    })


# A transcription of an example grammar used when explaining Lsystems.
shaked_lample = Lsystem('a', {
    'a': 'a+b',
    'b': 'b-a',
    '+': 'a+',
    'b': 'b-',
    })


cantor = Lsystem('a', {
    'a': 'aba',
    'b': 'bbb',
    })

levy = Lsystem('f', { 'f': '+f--f+', })


### 3d hilbert curve lsystem!?

hilbert3d = Lsystem('A', {
    'A': 'B-F+CFC+F-D&F.D-F+&&CFC+F+B',
    'B': 'A&F.CFB.F.D..-F-D.|F.B|FC.F.A',
    'C': '|D.|F.B-F+C.F.A&&FA&F.C+F+B.F.D',
    'D': '|CFB-F+B|FA&F.A&&FB-F+B|FC',
    })



if __name__ == "__main__":
    #print(binary_tree(8))
    #print(lsx(koch_curve2(), 5))
    #print(hilbert2.generate(5))

    #print('\n1: ' + levy.generate(1))
    #print('\n1: ' + levy.generate(2))
    #print('\n4: ' + levy.generate(4))              
    #print('\n7: ' + levy.generate(7))
    #print('\n10: ' + levy.generate(10))

    #h = hilbert3d.generate(8)
    #h = hilbert3d
    #print(h.alphabet())

    a1 = stoch1.generate(5)
    a2 = stoch1.generate(5)
    print(a1)
    print(a2)



    #print(levy.generate(13))
