# Python By Example Book
# Challenge 088 - Ask the user for a list of five integers. Store them in an array. Sort the list
# and display it in reverse order.

from array import *

nums = array('i', [])

for y in range (0,5):
    newValue = int(input("Enter a number: "))
    nums.append(newValue)

nums = sorted(nums)
nums.reverse()

print (nums)