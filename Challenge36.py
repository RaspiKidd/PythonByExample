# Python By Example Book
# Challenge 036 - Alter program 35 so that it will ask the user to enter their name and a number
# and then display their name that number of times.

name = input("What is your name? ")
num = int (input("Enter a number: "))

for i in range (0,num):
    print(name)