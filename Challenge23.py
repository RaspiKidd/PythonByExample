# Python By Example Book
# Challenge 023 - Ask the user to type in the first line of a nursery rhyme and display the length of the string.
# Ask for a starting number and an ending number and then display just that selection of the text (python starts counting at 0).

rhyme = input("enter a line from a nursery rhyme: ")

length = len(rhyme)

print("this has", length, "letters in it")

start = int(input("Enter a starting number: "))
end = int(input("Enter a end number: "))

print(rhyme [start:end])