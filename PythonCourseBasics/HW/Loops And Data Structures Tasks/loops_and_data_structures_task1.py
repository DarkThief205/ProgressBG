# ---------------------------------- Task 1 ---------------------------------- #
""" DESCRIPTION:
    Write a program that takes an integer n and prints a triangle pattern of stars (*). The number of stars in the first line is 1, in the second line is 2, and so on up to n stars in the n-th line.
"""

### Your code here

n = int(input("Enter stars number: "))


for i in range(1, n + 1):
    print('*' * i)

### EXPECTED OUTPUT:
# Enter stars number: 4
# *
# **
# ***
# ****
# ---------------------------------------------------------------------------- #

