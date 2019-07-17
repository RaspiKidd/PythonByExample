# Python By Example Book
# Challenge 082 - Show the user a line of text from your favourite poem and ask for a starting and an ending point.
# Display the characters between those two points.

poem = "Oh, I wish I'd looked after my teeth,"
print (poem)

start = int(input("enter a starting number: "))
end = int(input("enter an ending number: "))

print (poem[start:end])