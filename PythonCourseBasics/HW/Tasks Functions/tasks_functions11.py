# ---------------------------------- Task 11 ---------------------------------- #
""" DESCRIPTION:
Write a lambda expression 'sort_by_last_letter' that sorts a list of strings based on
the last letter of each string. Use this lambda expression to sort a given list,
using the sorted() built-in function.
"""
sort_by_last_letter = lambda word: word[-1]

### TEST:
print(sorted(["cherry", "banana", "apple"], key=sort_by_last_letter)) #Sorts the list of strings based on the last letter

### EXPECTED OUTPUT:
# ['banana', 'apple', 'cherry']

# ---------------------------------------------------------------------------- #
