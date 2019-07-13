# Python By Example Book
# Challenge 066 - Draw an octagon that uses a different colour (randomly selected from 6 possible colours)
# for each line.

import turtle
import random

turtle.shape ("turtle")
turtle.pensize (3)

for i in range (0, 8):
    turtle.color (random.choice(["red", "blue", "yellow", "green", "pink", "orange"]))
    turtle.forward (50)
    turtle.right (45)

turtle.exitonclick ()
