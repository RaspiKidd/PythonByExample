# Python By Example Book
# Challenge 049 - Create a variable called compNum and set the value to 50.
# Ask the user to enter a number. While their guess is not equal to the compNum
# tell them if there guess is too low or too and ask them to have another go.
# If they enter the same value as compNum, display the message "Well done, you took (count) attempts".

count = 0
compNum = 50
guess = int(input("Can you guess the number I am thinking of? "))

while guess != compNum:
    if guess < compNum:
        print ("Too Low")
    else:
        print ("Too High")
    count = count + 1
    guess = int(input("have another guess: "))
print ("Well done, you took", count, "attempts")