# Python By Example Book
# Challenge 028 - Update program 27 so that it will display the answer to two decimal places.

num = float(input("Enter a number with alot of decimal places: "))
answer = num*2

print(round(answer, 2))