# Python By Example Book
# Challenge 076 - Ask the user to enter the names of three people they want to invite to a party and store them in a list.
# After they have entered all three names, ask them if they want to add another. If they do, allow them to add more names
# until they answer "no". When they answer "no", display how many people they have invited to the party.

name1 = input("Enter the name of somebody you want to invite to your party: ")
name2 = input("Enter another name: ")
name3 = input("Enter another name: ")
party = [name1, name2, name3]
another = input("Do you want to invite another? (y/n) ")

while another == "y":
    newname = party.append(input("Enter another name: "))
    another = input("Do you want to invite another? (y/n) ")
print ("You have", len(party), "people coming to your party")