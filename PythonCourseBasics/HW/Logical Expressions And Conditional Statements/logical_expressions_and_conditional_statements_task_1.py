# logical_expressions_and_conditional_statements_tasks.py

# ---------------------------------- Task 1 ---------------------------------- #
# """ DESCRIPTION:
#     Write a program that takes a number as input and checks if it is positive, negative, or zero.
# """

### Your code here
number = float(input("Enter a number: "))
if number > 0:
    print(f"Number {number:g} is positive.")
elif number < 0:
    print(f"Number {number:g} is negative.")
else:
    print(f"Number {number:g} is zero.")
### EXPECTED OUTPUT:
# "Enter a number: -2.45"
# "Number -2.45 is negative."
# -------------------------------------------------------------------------- #
