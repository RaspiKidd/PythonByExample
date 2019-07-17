# Python By Example Book
# Challenge 084 - Ask the user to type in their postcode. Display the first 2 letters in uppercase.

postcode = input("Enter your postcode: ")

start = postcode[0:2]
print (start.upper())