# Python By Example Book
# Challenge 069 - Create a tuple containing the names of five countries and display the whole tuple.
# Ask the user to enter one of the coutries that have been shown to them and then display the index number
# (i.e. position in the list) of that item in the tuple.

countries = ("Canada", "Scotland", "Australia", "America", "India")

print (countries)
print ()

country = input ("Enter the name of one of the countries: ")

print (country, "has index number", countries.index(country))