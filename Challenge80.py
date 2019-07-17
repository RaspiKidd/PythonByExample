# Python By Example Book
# Challenge 080 - Ask the user to enter their first anme and then display the length of their first name. Then ask for their surname
# and display the length of their surname. Join their first name and surname together with a space between and display the result.
# Finally display the length of their full name (including space).

firstName = input("Enter your first name: ")
print ("That has", len(firstName), "characters in it")

surname = input("Enter your surname: ")
print ("That has", len(surname), "characters in it")

name = firstName + " " + surname
print ("Your full name is", name)
print ("That has", len(name), "character in it")