# Python By Example Book
# Challenge 039 - Ask the user to enter a number between 1 and 12 and ten display the times table for that number.

num = int (input("Enter a number: "))

for i in range(1,12):
    answer = i * num
    print(i, "x", num, "=", answer)