# Python By Example Book
# Challenge 021 - Ask the user to enter their first name and then ask them to enter their surname.
# join them together with a space between and display the name and the length of whole name.

firstname = input("Enter your first name: ")
surname = input("Enter your surnname: ")

name = firstname + " " + surname
length = len(name)

print(name)
print(length)