# Python By Example Book
# Challenge 094 - Display an array of five numbers. Ask the user to select one of the numbers.
# Once they have selected a number, display the position of that item in the array.
# If they enter something that is not in the array, ask them to try again until the select a relevant item.

from array import *

nums = array('i', [4, 6, 8, 2, 5])

for i in nums:
    print (i)

num = int(input("Select a number from the array: "))

tryAgain = True

while tryAgain == True:
    if num in nums:
        print ("This number is in position", nums.index(num))
        tryAgain = False
    else:
        print("Not in array")
        num = int(input("Select a number from the array: "))