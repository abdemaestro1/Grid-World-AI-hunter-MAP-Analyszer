# click . py
from graphics import *
def main () :
 win = GraphWin ( " Click Me ! " )
 for i in range ( 10) :
  p= win.getMouse ( )
  print("You clicked at:", p.getX(), p.getY( ) )

win=GraphWin("test",500,500)
coordination_point1=win.getMouse()
coordination_point1.draw(win)
coordination_point2= win . getMouse ( )
coordination_point2.draw (win)
coordination_point3= win . getMouse ( )
coordination_point3. draw (win)

triangle=Polygon(coordination_point1,coordination_point2,coordination_point3)
triangle.draw(win).setOutline("red")
triangle
win.getMouse()
win.close()
