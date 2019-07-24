# Python By Example Book
# Challenge 089 - Create an array that will store a list of integers. Generate five random numbers and store them in the array.
# Display the array (showing each item on a seperate line)

from array import *
import random

nums = array('i', [])

for y in range (0,5):
    num = random.randint(1, 100)
    nums.append(num)

for y in nums:
    print (y)