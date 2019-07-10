# Python By Example Book
# Challenge 038 - Change program 37 to also ask for a number. Display their name (one letter at a time on each line)
# and repeat this for the number of times they entered.

name = input("What is your name? ")
num = int (input("Enter a number: "))

for x in range(0, num):
    for i in name:
        print(i)