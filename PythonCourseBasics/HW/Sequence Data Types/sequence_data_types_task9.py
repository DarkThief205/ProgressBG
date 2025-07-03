# ---------------------------------- Task 9 ---------------------------------- #
# """ DESCRIPTION:
#     Write a program that asks the user to enter a word and then checks if the word is a palindrome.
#     A palindrome is a word that reads the same forward and backward, ignoring case.

#     Tip: you can use str.lower() to convert a string to lowercase
# """

### Your code here
word = input("Enter a word: ")
word_lower = word.lower()

if word_lower == word_lower[::-1]:
    print(f"The word '{word}' is a palindrome")
else:
    print(f"The word '{word}' is not a palindrome")

### EXPECTED OUTPUT:
# Enter a word : Racecar
# The word 'Racecar' is a palindrome

# Enter a word : car
# The word 'car' is not a palindrome
# ---------------------------------------------------------------------------- #
