# ---------------------------------- Task 5 ---------------------------------- #
# """ DESCRIPTION:
#     Write a program that asks the user to enter a word.
#     Create a new string 'reversed_word' that contains the word in reverse order using slicing.

#     TIP: Use slicing with a negative step to reverse a string.
# """

### Your code here
user_word = input("Enter a word: ")
reversed_word = user_word[::-1]

print(reversed_word)

### EXPECTED OUTPUT:
# Enter a word: Python
# Reversed word: nohtyP
# ---------------------------------------------------------------------------- #
