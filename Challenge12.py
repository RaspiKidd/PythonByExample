# Python By Example Book
# Challenge 012 - Ask for two numbers. If the first one is larger than the second, display the second number first and then the first number,
# otherwise show the first number first then the second number.

num1 = int(input("Enter a number: "))
num2 = int(input("Enter another number: "))

if num1 > num2:
    print(num2, num1)
else:
    print(num1, num2)