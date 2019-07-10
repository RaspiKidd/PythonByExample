# Python By Example Book
# Challenge 031 - Ask the user to enter the radius of a circle (measurement from the centre point to the edge).
# Workout the area of the circle.

import math

radius = int(input("Enter the radius of a circle: "))

area = math.pi*(radius**2)

print (area)