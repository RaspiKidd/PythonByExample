# Python By Example Book
# Challenge 078 - Create a list containing the titles of four TV programmes and display them on seperate lines.
# Ask the user to enter another show and a position they want it inserted into the list. Display the list again
# showing all five TV programmes in their new positions.

tv = ["Saddow Hunters", "Jane the virgin", "The big bang theory", "How I met your mother"]

for i in tv:
    print (i)
print ()
newtv = input("Enter another TV show: ")
position = int(input("ENter a number between 0 and 3: "))
tv.insert(position, newtv)
for i in tv:
    print (i)