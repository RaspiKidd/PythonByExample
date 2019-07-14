# Python By Example Book
# Challenge 072 - Create a list of six school subjects. Ask the user which of these subjects they
# don't like. Delete the subject they have chosen from the list before you display the list again.

subjects = ["maths", "english", "p.e", "computing", "science", "history"]
print (subjects)
print ()

dislike = input("Which subject do you not like? ")
delete = subjects.index(dislike)

del subjects [delete]

print (subjects)