# ---------------------------------- Task 2 ---------------------------------- #
""" DESCRIPTION:
Create a function 'is_even' that takes a single integer argument and returns True
if the number is even, and False otherwise.
"""

### YOUR CODE HERE

def is_even(number):
    if number % 2 == 0:
        print("True")
    else:
        print("False")
    return

print(is_even(4))
print(is_even(5)) 
### TEST:
# print(is_even(4))
# print(is_even(5))

### EXPECTED OUTPUT
# True
# False
# ---------------------------------------------------------------------------- #
