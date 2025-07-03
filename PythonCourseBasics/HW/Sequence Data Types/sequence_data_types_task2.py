# ---------------------------------- Task 2 ---------------------------------- #
# """ DESCRIPTION:
#     Write a program that asks the user to enter a list of numbers separated by spaces.
#     Then, ask for two indices 'start' and 'end' to slice the list.
#     Create a new list 'sliced_list' containing elements from 'start' to 'end' (excluding 'end').

#     TIP: Use list slicing syntax list[start:end] to extract a sublist.
# """

### Your code here

entered_numbers = input("Enter numbers separated by spaces: ") # int() Throws error: "ValueError: invalid literal for int() with base 10: '1 2 3 4 5 6 7 8 9'"
numbers = list(map(int, entered_numbers.split()))
start_index = int(input("Enter start index: "))
end_index = int(input("Enter end index: "))
sliced_list = numbers[slice(start_index, end_index)]
print("Sliced list:", sliced_list)

### EXPECTED OUTPUT:
# Enter numbers separated by spaces: 1 2 3 4 5 6 7 8 9
# Enter start index: 2
# Enter end index: 6
# Sliced list: [3, 4, 5, 6]
# ---------------------------------------------------------------------------- #
