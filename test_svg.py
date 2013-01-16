import svgwrite


import pysvg.structure
import pysvg.builders
import pysvg.text


import svgwrite


def test_pysvg():
    svg = pysvg.structure.Svg()
    shape_builder = pysvg.builders.ShapeBuilder()
    svg.addElement(shape_builder.createRect(0, 0, 
                                            "200px", "100px",
                                            strokewidth=1,
                                            stroke='black',
                                            fill="rgb(255, 255, 0)"))
    svg.addElement(pysvg.text.Text("Hello World", x = 210, y = 110))
    #print(svg_document.getXML())
    svg.save("test_pysvg.svg")

def test_svgwrite():
    dwg = svgwrite.Drawing('test_svgwrite.svg', profile='tiny')
    dwg.add(dwg.line((0, 0), (10, 0), stroke=svgwrite.rgb(10, 10, 16, '%')))
    dwg.add(dwg.text('Test', insert=(0, 0.2), fill='red'))
    dwg.save()



if __name__ == "__main__":
    test_svgwrite()
    test_pysvg()
