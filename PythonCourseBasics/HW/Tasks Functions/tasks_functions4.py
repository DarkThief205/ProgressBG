# ---------------------------------- Task 4 ---------------------------------- #
""" DESCRIPTION:
Create a function 'count_vowels' that takes a string and returns the count of vowels (a, e, i, o, u) in the string.
"""


### YOUR CODE HERE
vowels = ("aeiou")
def count_vowels(word):
    return sum(1 for char in word if char in vowels) #adds 1 to each vowel
    
print(count_vowels("hello"))
print(count_vowels("world"))
### TEST:
# print(count_vowels("hello"))
# print(count_vowels("world"))

### EXPECTED OUTPUT:
# 2
# 1
# ---------------------------------------------------------------------------- #
