
x = int(input("Enter the first point 'x' "))
y = int(input("Enter the second point 'y' "))
x1 = int(input("Enter the third point 'x1' "))
y1 = int(input("Enter the fourth point 'y1' "))

import math

dist = math.sqrt((x - x1)** 2 + (y - y1)** 2)

print  "The distance between 'x','x1' and 'y','y1' is",  dist
