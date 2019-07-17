# Python By Example Book
# Challenge 086 - Ask the user to enter a new password. Ask them to enter it again. If the two passwords
# match, display "Thank you". If the letters are correct but in the wrong case, display the message
# They must be in the same case", otherwise display the message "Incorrect".

pswd1 = input("Enter a password: ")
pswd2 = input("Enter it again: ")

if pswd1 == pswd2:
    print ("Thank you")
elif pswd1.lower() == pswd2.lower():
    print ("They must be the same case")
else:
    print ("Incorrect")