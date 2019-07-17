# Python By Example Book
# Challenge 087 - Ask the user to type in a word and then display it backwards on seperate lines.
# For instance, if they type in "Hello" it should display as shown below:
'''
Enter a word: Hello
o
l
l
e
H
'''

word = input("Enter a word: ")
length = len(word)
num = 1

for x in word:
    position = length - num
    letter = word[position]
    print (letter)
    num = num + 1