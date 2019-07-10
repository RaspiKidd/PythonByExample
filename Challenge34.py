# Python By Example Book
# Challenge 034 - Display the following message:
# 1) Square
# 2) Triangle
# Enter a number:
# If the user enters 1, then it should ask them for the length of one of its sides and display the area.
# If they select 2, it should ask for the base and height of the triangle and display the area.
# If they type in anything else it should give them a suitable error message.

print("1) Square")
print("2) Triangle")
print()

menuSelection = int(input("Enter a number: "))

if menuSelection == 1:
    side = int(input("Enter the length of one side: "))
    area = side*side
    print("The area of the square is", area)
elif menuSelection == 2:
    base = int(input("Enter the length of the base: "))
    height = int(input("Enter the height of the triangle: "))
    area = (base*height)/2
    print("The area of the triangle is", area)
else:
    print("Incorrect option selected")