# Python By Example Book
# Challenge 044 - Ask how many people the user wants to invite to a party. If they enter a number below 10.
# ask for the names and after each name display "(name) has to be invited to the party". If they enter a number which is
# 10 or higher display the message "Too many people".

invite = int(input("How many people are coming to the party? "))

if invite < 10:
    for i in range (0, invite):
        name = input("what is their name? ")
        print(name, "has been invited")
else:
    print("Too many people")