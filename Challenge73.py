# Python By Example Book
# Challenge 073 - Ask the user to enter four of their favourite foods and store them in a dictionary
# so that they are indexed with numbers starting from 1. Display the dictionary in full, showing the index number and the item.
# Ask them which they want to get rid of and remove it. Sort the remaining data and display the dictionary.

food = {}

food1 = input("Enter a food you like: ")
food[1] = food1

food2 = input("Enter another food you like: ")
food[2] = food2

food3 = input("Enter another food: ")
food[3] = food3

food4 = input("and another: ")
food[4] = food4

print (food)

dislike = int(input("Which one would you like to get rid of? "))

del food[dislike]

print (sorted(food.values()))