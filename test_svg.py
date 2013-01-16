#import svgwrite
"""
dwg = svgwrite.Drawing('test.svg', profile='tiny')
dwg.add(dwg.line((0, 0), (10, 0), stroke=svgwrite.rgb(10, 10, 16, '%')))
dwg.add(dwg.text('Test', insert=(0, 0.2), fill='red'))
dwg.save()
"""

import pysvg


if __name__ == "__main__":
    pysvg.SVG('test')
    t = pysvg.Text('Hello', 0, 200)
    svg.addElement(t)
    svg.saveSVG('test.svg')
