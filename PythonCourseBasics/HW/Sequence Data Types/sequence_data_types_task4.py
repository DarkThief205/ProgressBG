# ---------------------------------- Task 4 ---------------------------------- #
# """ DESCRIPTION:
#     Write a program that generates a list of numbers from 100 to 50 (inclusive), counting down by 5.
#     Then, create a new list 'first_half' that contains only the first half of this list using slicing.

#     TIP: Use range(start, stop, step) to create the initial list.
#         Use slicing to extract the first half.
# """

### Your code here
list_numbers = list(range(100, 49, -5))
first_half_numbers = list_numbers[slice(0, 6)]

print("Original list:", list_numbers)
print("First half:", first_half_numbers)

### EXPECTED OUTPUT:
# Original list: [100, 95, 90, ..., 50]
# First half: [100, 95, 90, ..., 75]
# ---------------------------------------------------------------------------- #
