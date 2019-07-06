# Python By Example Book
# Challenge 005 - Ask the user to enter 3 numbers. Add together the first 2 numbers and then multiply this total by the third number. Display the answer as The answer is [answer]

num1 = int(input("Enter a number: "))
num2 = int(input("Enter another number: "))
num3 = int(input("Enter a third number: "))
total = (num1 + num2)*num3

print("The total is" , total)