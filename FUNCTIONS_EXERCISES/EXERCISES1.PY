#GEOMETRY & MATH MULTI SOLVER 
''''
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from graphics import *
from math import *

def analyze_triangle(x1, y1, x2, y2, x3, y3):
    #ENTER first point
    x=float(input("Enter the (x) coordination of the first point :"))
    y=float(input("Enter the (y) coordination of the first point :"))
    a=Point(x,y)

    #ENTER second point
    w=float(input("Enter the (x) coordination of the first point :"))
    z=float(input("Enter the (y) coordination of the first point :"))
    b=Point(w,z)

    #ENTER third point
    h=float(input("Enter the (x) coordination of the first point :"))
    j=float(input("Enter the (y) coordination of the first point :"))
    c=Point(h,j)

    #DISTANCE between sides 
    d1=sqrt( (w-x)**2 + (z-y)**2 )
    d2=sqrt( (h-x)**2 + (j-y)**2 )
    d3=sqrt( (w-h)**2 + (z-j)**2 )

    #Perimeter
    Peri=d1+d2+d3

    #AREA
    semi=Peri/2
    Area=sqrt(semi*(semi-d1)*(semi-d2)*(semi-d3))

    return d1,d2,d3,semi,Area

analyze_triangle(0,2,1,3,2,2)
'''
import math

def analyze_triangle(x1, y1, x2, y2, x3, y3):
    # 1. Calculate the three side lengths
    d1 = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    d2 = math.sqrt((x3 - x2)**2 + (y3 - y2)**2)
    d3 = math.sqrt((x1 - x3)**2 + (y1 - y3)**2)

    # 2. Calculate Perimeter
    peri = d1 + d2 + d3

    # 3. Calculate Area via Heron's Formula
    semi = peri / 2
    area = math.sqrt(semi * (semi - d1) * (semi - d2) * (semi - d3))

    # 4. Return side lengths, perimeter, and area
    return d1, d2, d3, peri, area


# --- Execution & Unpacking Example ---

# Hardcoded coordinates
s1, s2, s3, perimeter, area = analyze_triangle(0, 2, 1, 3, 2, 2)

print(f"Side 1: {s1:.2f}")
print(f"Side 2: {s2:.2f}")
print(f"Side 3: {s3:.2f}")
print(f"Perimeter: {perimeter:.2f}")
print(f"Area: {area:.2f}")