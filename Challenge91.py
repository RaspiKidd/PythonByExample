# Python By Example Book
# Challenge 091 - Create an array which contains five numbers (two of which should be repeated).#
# Display the whole array to the user. Ask the user to enter one of the numbers from the array and then
# display a message saying how many times thst number appears in the list.

from array import *

nums = array('i', [5, 7, 9, 2, 7])

for y in nums:
    print (y)

num = int(input("Enter a number thats in the list: "))

if nums.count (num) == 1:
    print (num, "is in the list once")
else:
    print (num, "is in the list", nums.count(num), "times")