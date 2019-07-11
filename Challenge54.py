# Python By Example Book
# Challenge 054 - Randomly chose heads or tails ("h" or "t"). Ask the user to make their choice.
# If their choice is the same as the randomly selected value, display the message "You win",
# otherwise display "bad luck". At the end, tell the user if the computer selected heads or tails.

import random

coin = random.choice(["h", "t"])
guess = input("Enter (h)eads or (t)ails: ")

if guess == coin:
    print ("You win")
else:
    print ("Bad luck")
if coin == "h":
    print ("It was heads")
else:
    print ("It was tails")