# Python By Example Book
# Challenge 071 - Create a list of two sports. Ask the user what their favourite sport is and
# add it to the end of the list . Sort the list and display it.

sports = ["Baseball", "Running"]

sports.append (input("What is your favourite sport? "))

print (sorted(sports))