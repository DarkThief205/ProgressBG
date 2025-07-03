# ---------------------------------- Task 6 ---------------------------------- #
# """ DESCRIPTION:
#     Write a program that generates a list of numbers from 10 to 100 with a step of 10.
#     Then, create a new list 'middle_part' containing all elements except the first and last two using slicing.

#     TIP: Use range(start, stop, step) to create the initial list.
#          Use slicing to remove the first and last two elements.
# """

### Your code here
number_list = list(range(10, 101, 10))
middle_part = number_list[2:-2] 
print("Original list:", number_list)
print("Middle part:", middle_part)


### EXPECTED OUTPUT:
# Original list: [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
# Middle part: [30, 40, 50, 60, 70, 80]
# ---------------------------------------------------------------------------- #
