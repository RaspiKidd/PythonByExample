# Python By Example Book
# Challenge 006 - Ask how many slices of pizza the user started with and ask how many slices they have eaten.
# Work out how many slices they have left and display the answer in a user friendly format.

startedWith = int(input("How many slices of pizza? "))
eaten = int(input("How many slices have you eaten? "))
left = startedWith - eaten

print ("You have", left, "slices of pizza left")