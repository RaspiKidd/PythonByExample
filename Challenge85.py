# Python By Example Book
# Challenge 085 - Ask the user to enter their name and tell them how many vowels are in their name.

name = input("Enter your name: ")
count = 0
name = name.lower()

for x in name:
    if x == "a" or x == "e" or x == "i" or x == "o" or x == "u":
        count = count + 1
print ("Vowels =", count)