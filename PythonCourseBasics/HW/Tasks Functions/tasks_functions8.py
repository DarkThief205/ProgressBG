# ---------------------------------- Task 8 ---------------------------------- #
""" DESCRIPTION:
Write a lambda function 'is_palindrome' that checks if a given string is a palindrome.
"""
is_palindrome = lambda s: s == s[::-1]

### TEST:
print(is_palindrome("madam"))
print(is_palindrome("hello"))

### EXPECTED OUTPUT:
# True
# False
# ---------------------------------------------------------------------------- #
