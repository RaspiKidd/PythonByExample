# Python By Example Book
# Challenge 077 - Change program 076 so that once the user has completed their list of names, display the full list
# and ask them to type in one of the names on the list. Display the position of that name in the list. Ask the user
# if they still want that person to come to the party, if they answer "no", delete that entry from the list and display
# the list again.

name1 = input("Enter the name of somebody you want to invite to your party: ")
name2 = input("Enter another name: ")
name3 = input("Enter another name: ")
party = [name1, name2, name3]
another = input("Do you want to invite another? (y/n) ")

while another == "y":
    newname = party.append(input("Enter another name: "))
    another = input("Do you want to invite another? (y/n) ")
print ("You have", len(party), "people coming to your party")
print (party)
selection = input("Enter one of the names: ")
print (selection, "is in position", party.index(selection),"on the list")
stillCome = input("Do you still want them to come? (y/n) ")
if stillCome == "n":
    party.remove(selection)
print (party)