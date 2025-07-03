
# ---------------------------------- Task 3 ---------------------------------- #
# """ DESCRIPTION:
#     Write a program that generates a list of numbers from 1 to 50 using range().
#     Then, create a new list 'evens' that contains only the even numbers from this list using slicing.

#     TIP: Use range(start, stop) to create the initial list.
#         Use slicing with a step to extract every second element.
# """

### Your code here

original_numbers = list(range(1,51))
even_numbers = original_numbers[1:51:2]
print("Original list: ", original_numbers)
print("Even numbers: ", even_numbers)

### EXPECTED OUTPUT:
# Original list: [1, 2, 3, ..., 50]
# Even numbers: [2, 4, 6, ..., 50]
# ---------------------------------------------------------------------------- #