import math
print("!!!!WARNING:A must be not equal to X!!!!")
x,y=eval(input("Enter your first point cordination X,Y (separate with comun,):"))
a,b=eval(input("enter your second point cordination A,B (separate with comun,):"))
Distance=math.sqrt((x-a)**2+(y-b)**2)
Slope=(y-b)/(x-a)
print(f"the distance between them is {Distance:.2f}cm")
print(f"the slope is {Slope:.2f}cm")



