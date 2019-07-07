# Python By Example Book
# Challenge 025 - Ask the user to enter their first name. If the length of their first name is under 5 characters, ask them to enter
# their surname and join them together (without a space) and display the name in uppercase. If the length of the first name is 5 characters
# or more display their first name in lowercase.

firstname = input("Enter your first name: ")

if len(firstname) < 5:
    surname = input("Enter your surname: ")
    name = firstname+surname
    print(name.upper())
else:
    print(firstname.lower())