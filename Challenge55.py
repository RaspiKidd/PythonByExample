# Python By Example Book
# Challenge 055 - Randomly choose a number between 1 and 5. Ask the user to pick a number.
# If they guess correctly, display the message "Well done", otherwise tell them if they are too high
# or too low and ask them to pick a second number. If they guess correctly on their second guess, display
# "Correct", otherwise display "You lose".

import random

num = random.randint(1, 5)
guess = int(input("Enter a number: "))

if guess == num:
    print ("You win")
elif guess > num:
    print ("Too high")
    guess = int(input("Have another go: "))
    if guess == num:
        print ("Correct")
    else:
        print ("You lose")
elif guess < num:
    print ("Too Low")
    guess = int(input("Have another go: "))
    if guess == num:
        print ("Correct")
    else:
        print ("You lose")