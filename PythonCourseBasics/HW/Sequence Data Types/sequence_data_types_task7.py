# ---------------------------------------------------------------------------- #

# ---------------------------------- Task 7 ---------------------------------- #
# """ DESCRIPTION:
#     Write a program that asks the user to enter a sentence.
#     Create a new string 'every_second_char' that contains every second character from the sentence using slicing.

#     TIP: Use slicing with a step to extract every second character.
# """

### Your code here
sentence = input("Enter a sentence: ")
every_second_char = sentence[::2]
print("Every second character:", every_second_char)

### EXPECTED OUTPUT:
# Enter a sentence: Python slicing is powerful!
# Every second character: Pto lcn spwru!