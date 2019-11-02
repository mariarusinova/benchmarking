from bs4 import BeautifulSoup
from bs4.element import Tag

seed = """
<mxGraphModel 
    dx="1422" 
    dy="767" 
    grid="1" 
    gridSize="10" 
    guides="1" 
    tooltips="1" 
    connect="1" 
    arrows="1" 
    fold="1" 
    page="1" 
    pageScale="1" 
    pageWidth="2100" pageHeight="2970" math="0" shadow="0">
  <root>
    <mxCell id="0"/>
    <mxCell id="1" parent="0"/>
  </root>
</mxGraphModel>
"""

graph = BeautifulSoup(seed, features="xml")

py = open('stage6.py').readlines()

place = graph.find('mxCell', parent="0")

class MxGeometry(Tag):
    def __init__(self, x=None, y=None, width=None, height=None):
        try:
            assert x != None
            super().__init__(
                name = 'mxGeometry', 
                attrs = {
                    'x' :      x, 
                    'y' :      y, 
                    'width' :  width, 
                    'height':  height, 
                    'as' :     "geometry"
                }
            )
        except AssertionError:
            super().__init__(
                name = 'mxGeometry', 
                attrs = {
                    'relative':"1",
                    'as' :     "geometry"
                }
            )
            
class Block(Tag):
    def __init__(self, tag, codeline):
        super().__init__(name = tag)
    
class LoadBlock(Block):
    def __init__(self, codeline):
        super().__init__('load', codeline)

class CalcBlock(Block):
    def __init__(self, codeline):
        super().__init__('calc', codeline)

class DumpBlock(Block):
    def __init__(self, codeline):
        super().__init__('dump', codeline)

class OtherBlock(Tag):
#      <mxGeometry x="260" y="320" width="100" height="100" as="geometry"/>
    def __init__(self, codeline, id = 0):
        super().__init__(
            name = 'mxCell',
            attrs = {
                'id':id,
                'style':"rounded=1;whiteSpace=wrap;html=1;absoluteArcSize=1;arcSize=14;strokeWidth=2;fontSize=14;",
                'vertex':"1"
            }
        )
        mxGeometry = MxGeometry()
        self.insert(new_child = mxGeometry, position = 0)
        
for line in py:
    try:
        line.index('load(')
        block = LoadBlock(line)
    except ValueError:
        try:
            line.index(' = ')
            block = CalcBlock(line)
        except ValueError:
            try:
                line.index('dump(')
                block = DumpBlock(line)
            except ValueError:
                block = OtherBlock(line)
    place.insert_after(block)

print(graph.prettify())        
"""
<mxGraphModel dx="1422" dy="767" grid="1" gridSize="10" guides="1" tooltips="1" connect="1" arrows="1" fold="1" page="1" pageScale="1" pageWidth="827" pageHeight="1169" math="0" shadow="0">
  <root>
    <mxCell id="0"/>
    <mxCell id="1" parent="0"/>
    <mxCell 
      id="2" 
      style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;exitX=1;exitY=0.5;exitDx=0;exitDy=0;entryX=0;entryY=0.5;entryDx=0;entryDy=0;endArrow=classic;endFill=1;strokeWidth=2;fontSize=14;" 
      edge="1" 
      parent="1" 
      source="5" 
      target="3">
      <mxGeometry relative="1" as="geometry"/>
    </mxCell>
    <mxCell 
      id="3" 
      value="2" 
      style="rounded=1;whiteSpace=wrap;html=1;absoluteArcSize=1;arcSize=14;strokeWidth=2;fontSize=14;" 
      vertex="1" 
      parent="1">
      <mxGeometry x="260" y="320" width="150" height="80" as="geometry"/>
    </mxCell>
    <mxCell 
      id="4" 
      style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;exitX=1;exitY=0.5;exitDx=0;exitDy=0;exitPerimeter=0;entryX=0;entryY=0.5;entryDx=0;entryDy=0;endArrow=classic;endFill=1;strokeWidth=2;fontSize=14;" 
      edge="1" 
      parent="3" 
      source="6" 
      target="2">
      <mxGeometry relative="1" as="geometry"/>
    </mxCell>
    <mxCell 
      id="5" 
      value="1" 
      style="strokeWidth=2;html=1;shape=mxgraph.flowchart.database;whiteSpace=wrap;fontSize=14;" 
      vertex="1" 
      parent="1">
      <mxGeometry x="40" y="320" width="160" height="80" as="geometry"/>
    </mxCell>
    <mxCell 
      id="6" 
      value="3" 
      style="shape=internalStorage;whiteSpace=wrap;html=1;dx=15;dy=15;rounded=1;arcSize=8;strokeWidth=2;fontSize=14;" 
      vertex="1" 
      parent="1">
      <mxGeometry x="460" y="320" width="160" height="80" as="geometry"/>
    </mxCell>
  </root>
</mxGraphModel>

<mxGraphModel 
    dx="1422" 
    dy="767" 
    grid="1" 
    gridSize="10" 
    guides="1" 
    tooltips="1" 
    connect="1" 
    arrows="1" 
    fold="1" 
    page="1" 
    pageScale="1" 
    pageWidth="827" pageHeight="1169" math="0" shadow="0">
  <root>
    <mxCell id="0"/>
    <mxCell id="1" 
        parent="0"/>
    <mxCell id="2" 
        value="123" 
        style="shape=mxgraph.flowchart.terminator;whiteSpace=wrap;fontSize=14;strokeWidth=2;" 
        parent="1" 
        vertex="1">
      <mxGeometry x="400" y="50" width="100" height="50" as="geometry"/>
    </mxCell>
    <mxCell id="3" 
        value="123" 
        style="shape=mxgraph.flowchart.terminator;whiteSpace=wrap;fontSize=14;strokeWidth=2;" 
        parent="1" 
        vertex="1">
      <mxGeometry x="400" y="150" width="100" height="50" as="geometry"/>
    </mxCell>
    <mxCell id="4" 
        style="edgeStyle=orthogonalEdgeStyle;rounded=1;orthogonalLoop=1;jettySize=auto;html=1;exitX=0.5;exitY=1;exitDx=0;exitDy=0;exitPerimeter=0;entryX=0.5;entryY=0;entryDx=0;entryDy=0;entryPerimeter=0;fontSize=14;strokeWidth=2;endArrow=none;endFill=0;" 
        edge="1" 
        parent="1" 
        source="2" 
        target="3">
      <mxGeometry relative="1" as="geometry"/>
    </mxCell>  </root>
</mxGraphModel>
"""