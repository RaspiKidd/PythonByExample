# Python By Example Book
# Challenge 026 - Pig latin takes the first consonant of a word, moves it to the end of the word and adds on an "ay".
# If a word begins with a vowel you just add "way" to the end. For example, pig becomes igpay, banana becomes ananabay,
# and aadvark becomes aadvarkway. Create a program that will ask the user to enter a word and change it into Pig Latin.
# Make sure the new word is displayed in lowercase.

word = input("Enter a word: ")

first = word[0]
length = len(word)
rest = word [1:length]

if first != "a" and first != "e" and first != "i" and first != "o" and first != "u":
    newWord = rest + first + "ay"
else:
    newWord = word + "way"


print(newWord)