# Python By Example Book
# Challenge 070 - Add to program 069 to ask the user to enter a number and display the country in that position.

countries = ("Canada", "Scotland", "Australia", "America", "India")

print (countries)
print ()

country = input ("Enter the name of one of the countries: ")

print (country, "has index number", countries.index(country))

position = int(input("Enter a number between 0 and 4: "))

print (countries[position])