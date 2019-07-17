# Python By Example Book
# Challenge 081 - Ask the user to type i their favourite school subject. Display it with a "-" after each letter, e.g. S-p-a-n-i-s-h-.

favSubject = input("What is your favourite school subject: ")

for letter in favSubject:
    print (letter,end="-")