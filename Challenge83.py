# Python By Example Book
# Challenge 083 - Ask the user to type a word in uppercase. If they type it in lowercase, ask them to try again.
# Keep repeating this until they type in a message all in uppercase.

msg = input("Enter a message in uppercase: ")
tryAgain = False

while tryAgain == False:
    if msg.isupper():
        print ("thank you")
        tryAgain = True
    else:
        print ("Try again")
        msg = input("Enter a message in uppercase: ")