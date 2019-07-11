# Python By Example Book
# Challenge 048 - Ask for the name of somebody the user wants to invite to a party.
# After this, display the message "(name) has now been invited" and add 1 to the count.
# Then ask if they want to invite somebody else. Keep repeating this until they no longer
# want to invite anyone else to the party. and then display how many people they have
# coming to the party.

count = 0
again = "y"

while again == "y":
    name = input("Who do you want to invite to the party ")
    count = count + 1
    again = input("Would you like to invite another person? (y/n)")
print ("You have", count, "People coming to your party")