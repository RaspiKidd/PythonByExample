# Python By Example Book
# Challenge 057 - Update program 56 so that it tells the user if they are too hight
# or too low before they pick again.

import random

num = random.randint(1, 10)
correct = False

while correct == False:
    guess = int(input("Enter a number: "))
    if guess == num:
        correct = True
    elif guess > num:
        print ("Too high")
    else:
        print ("Too low")