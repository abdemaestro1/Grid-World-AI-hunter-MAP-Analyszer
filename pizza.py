import math
diametr= float(input("enter your pizza's diametre:"))
price=float(input("how much it costs ? "))
radius= diametr/2
Area=math.pi*(radius**2)
cost_per_inshe=math.fabs(price/Area)
print(f"the price is ${math.fabs(price)}, the diametre is {math.fabs(diametr)} inshes wide !")
print(f"the cost per insh is ${cost_per_inshe:.2f}")



