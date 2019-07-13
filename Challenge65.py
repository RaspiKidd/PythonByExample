# Python By Example Book
# Challenge 065 - Write the numbers 1, 2 and 3. Starting at the bottom of the number 1.

import turtle

turtle.shape ("turtle")

# No.1
turtle.left (90)
turtle.forward (100)
turtle.right (90)
turtle.penup ()
turtle.forward (50)
# No. 2
turtle.pendown ()
turtle.forward (75)
turtle.right (90)
turtle.forward (50)
turtle.right (90)
turtle.forward (75)
turtle.left (90)
turtle.forward (50)
turtle.left (90)
turtle.forward (75)
turtle.penup ()
turtle.forward (50)
# No. 3
turtle.pendown ()
turtle.forward (75)
turtle.left (90)
turtle.forward (50)
turtle.left (90)
turtle.forward (45)
turtle.left (180)
turtle.forward (45)
turtle.left (90)
turtle.forward (50)
turtle.left (90)
turtle.forward (75)

turtle.hideturtle ()

turtle.exitonclick ()