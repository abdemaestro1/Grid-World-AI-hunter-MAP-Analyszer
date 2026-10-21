#EXERCISE 2: Stacking stepsc with loop
from graphics import *
steps=int(input("ENTER the numbers of steps (bteween 3 and 8):"))

#CREAT the graphe
win=GraphWin("GRAPHE del 3ADAB lah ya5od l7a9",1500,900)
win.setCoords(0.0,0.0,17.0,9.0)

#SET the rectangles by the for loop
rect=Rectangle(Point(1.0,1.0),Point(16.0,0.0))
rect.setFill("red")
rect.draw(win)

first_point=rect.getP1()
second_point=rect.getP2()

first_x=first_point.getX()
first_y=first_point.getY()

second_x=second_point.getX()
second_y=second_point.getY()


for i in range(1,steps,1):

    first_x=first_x+1
    first_y=first_y+1

    second_x=second_x-1
    second_y=second_y+1

    new_rect=Rectangle(Point(first_x,first_y),Point(second_x,second_y))
    new_rect.setFill("red")
    new_rect.draw(win)
    

win.getMouse()
win.close()