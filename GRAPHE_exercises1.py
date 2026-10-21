#EXERCISE 1:the shape and the area visualizer 

from math import *
from graphics import *

print("********SHAPE & AREA VISUALIZER************")
#insert the inputs 
length_square=float(input("Enter the lenth of the square:"))
our_radius=float(input("enter the raidus of your circle (RAD < 0.5):"))

#calculatoins of the informations
Area_square=length_square**2
Area_circle=pi*(our_radius**2)

#CREAT THE GRAPHE
win=GraphWin("Shape Visualizer",500,500)
win.setCoords(0.0,0.0,2.0,3.0)

#DRAW the shapes in the graphe 

circle=Circle(Point(1.5,1.5),our_radius)
circle.setFill("blue")
circle.draw(win)

square=Rectangle(Point(0.5,1.5),Point(length_square,length_square))
square.setFill("green")
square.draw(win)

Text_area_circle=Text(Point(1.5,0.5),f"Area is: {Area_circle:.2f}")
Text_area_squar=Text(Point(0.5,0.5),f"Area is: {Area_square:.2f}")

Text_area_squar.draw(win)
Text_area_circle.draw(win)

Higher_value=0.0
if Area_square > Area_circle:
    Higher_value=Area_square
elif Area_square < Area_circle:
    Higher_value=Area_circle
else:
    Higher_value=Area_circle    

text_higher_area=Text(Point(1.0,2.5),f"The higher area is: {Higher_value:.2f}")
text_higher_area.draw(win)

win.getMouse()
win.close()
'''
import math 
from graphics import * 
def main():
  side = float(input("Enter side length of square: ")) 
  radius = float(input("Enter radius of circle: ")) 
  area_sq = side ** 2 
  area_circ = math.pi *(radius**2) 
  win = GraphWin("Shape Visualizer", 400, 400) 
  # Square on left side 
  sq = Rectangle(Point(50, 150), Point(50 + side, 150 + side))
  sq.setFill("skyblue")
  sq.draw(win)
   # Circle on right side 
  circ = Circle(Point(280, 200), radius) 
  circ.setFill("coral") 
  circ.draw(win) 
  # Summary Label 
  result_text = f"Square Area: {area_sq:.1f} | Circle Area: {area_circ:.1f}"
  label = Text(Point(200, 350), result_text)
  label.draw(win) 

  win.getMouse()  # Pause before closing
  win.close() 
main()
'''