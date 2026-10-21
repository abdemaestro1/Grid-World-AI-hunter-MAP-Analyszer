import graphics
from graphics import *

'''
#### Open a graphics window
win= GraphWin('Shapes')
#### Draw a red circle centered at point (100,100) with radius 30
center= Point(100,100)
circ = Circle(center, 30)
circ.setFill('red')
circ.draw(win)
 #### Put a textual label in the center of the circle
label= Text(center, "Red Circle")
label.draw(win)
 #### Draw a square using a Rectangle object
rect = Rectangle(Point(30,30), Point(70,70))
rect.draw(win)
 #### Draw a line segment using a Line object
line= Line(Point(20,30), Point(180, 165))
line.draw(win)
 #### Draw an oval using the Oval object
oval= Oval(Point(20,150),
Point(180,199))
oval.draw(win)
'''

print("***************Graphical programme***********")
#GET principale informations
principal=float(input("how much do you want to investigate:"))
apr=float(input("enter the annualized intrest rate:"))
#creat the graphe with a labels on the left side 
win=GraphWin("investement try graphic",1500,740)
win.setBackground("white")
Text(Point(50,710),"0.0k").draw(win)
Text(Point(50,550),"2.5k").draw(win)
Text(Point(50,370),"5.0k").draw(win)
Text(Point(50,200),"7.5k").draw(win)
Text(Point(50,30),"10.0k").draw(win)

#draw bar for initial principal 
tool=principal*0.06
bar=Rectangle(Point(100,710),Point(227,710-tool))
bar.setFill("green")
bar.setWidth(2)
bar.draw(win)

#draw bar for successive years
for y in range(1,11):
    #calculate value fir the next year
    principal=principal*(1+apr)
    #draw bar for this value
    x11=(y*127)+40
    hieght=principal*0.06
    bar=Rectangle(Point(x11,710),Point(x11+127,710-hieght))
    bar.setFill("green")
    bar.setWidth(2)
    bar.draw(win)
input("press <enter to quit>")
win.getMouse()
win.close()

