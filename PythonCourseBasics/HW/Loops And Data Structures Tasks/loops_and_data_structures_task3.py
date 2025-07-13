# ---------------------------------- Task 3 ---------------------------------- #
""" DESCRIPTION:
    Write a script that takes a list of strings and returns a dictionary,
    where each key is a string length and each value is a list of strings of that length.
"""

### Given:
words = ["hello", "world", "python", "is", "fun", "and", "useful"]

### Your code here

length_dict = {}

for word in words:
    length = len(word)
    if length not in length_dict:
        length_dict[length] = []
    length_dict[length].append(word)


print(length_dict)

### EXPECTED OUTPUT:
# {5: ['hello', 'world'], 6: ['python'], 2: ['is'], 3: ['fun', 'and'], 7: ['useful']}
# ---------------------------------------------------------------------------- #
