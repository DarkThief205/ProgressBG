# ---------------------------------- Task 7 ---------------------------------- #
""" DESCRIPTION:
Create a function 'remove_duplicates' that takes a list and removes duplicate elements, returning a new list with unique elements.
"""
def remove_duplicates(lst):
    return list(set(lst)) #set(Function in python)

### TEST:
print(remove_duplicates([1, 2, 2, 3, 4, 3]))

### EXPECTED OUTPUT:
# [1, 2, 3, 4]
# ---------------------------------------------------------------------------- #
