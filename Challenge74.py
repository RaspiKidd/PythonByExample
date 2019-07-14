# Python By Example Book
# Challenge 074 - Enter a list of 10 colours. Ask the user for a starting number between 0 and 4 and an end number
# between 5 and 9. Display the list for those colours between the start and end numbers the user input.

colours = ["red", "blue", "green", "black", "white", "pink", "grey", "purple", "yellow", "brown"]
start = int(input("Enter a starting number between 0 and 4: "))
end = int(input("Enter an end number beteen 5 and 9: "))

print (colours[start:end])