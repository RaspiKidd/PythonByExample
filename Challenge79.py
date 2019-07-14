# Python By Example Book
# Challenge 079 - Create an empty list called "nums". Ask the user to enter numbers. After each number is entered, add it to the end
# of the nums list and display the list. Once they have entered three numbers, ask them if they still want the last number they entered
# saved. If they say "no", remove the last item from the list. Display the list of numbers.

nums = []
count = 0

while count < 3:
    num = int(input("Enter a number:" ))
    nums.append(num)
    print (nums)
    count = count + 1
lastNum = input("Do you want the last number saved? (y/n) ")
if lastNum == "n":
    nums.remove(num)
print (nums)