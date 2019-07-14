# Python By Example Book
# Challenge 075 - Create a list of four three digit numbers. Display the list to the user, showing each item
# from the list on a seperate line. Ask the user to enter a three digit number. If the number they have typed in matches one in the list
# display the position of that number in the list, otherwise display the message "That is not in the list".

numbers = [123, 432, 567, 987]

for i in numbers:
    print (i)

num = int(input("Enter a three digit number: "))

if num in numbers:
    print (num, "is in position", numbers.index(num))
else:
    print ("That is not in the list")