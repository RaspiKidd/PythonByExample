# Python By Example Book
# Challenge 033 - Ask the user to enter two numbers. Use whole number division to divide the first number by the second number
# and also work out the remainder and display the answer in a user friendly way.
# (if they enter 7  and 2 display 7 divided by 2 is 3 with 1 remaining)

num1 = int(input("Enter a number: "))
num2 = int(input("Enter another number: "))

divide = num1 // num2
remainder = num1 % num2

print (num1, "divided by", num2, "is", divide, "with", remainder, "remaining")