# ---------------------------------- Task 8 ---------------------------------- #
# """ DESCRIPTION:
#     Write a program which will ask the user to enter 3 names.
# 	The names, should be stored into a list 'names'.
#     Create another list 'sorted_names' which will have names, sorted alphabetically. Do not change the original 'names' list.

#     TIP: use list.sort() method to sort a list. Note, that the sort() method works "in-place",
# """

### Your code here

name1 = input("Enter 1st name: ")
name2 = input("Enter 2d name: ")
name3 = input("Enter 3d name: ")

names = [name1, name2, name3]
sorted_names = names.copy()
sorted_names.sort()

print("Originally entered names:", names)
print("Sorted names:", sorted_names)

### EXPECTED OUTPUT:
# Enter 1st name: Maria
# Enter 2d name: Ivan
# Enter 3d name: Asen

# Originally entered names:  ['Maria', 'Ivan', 'Asen']
# Sorted names: ['Asen', 'Ivan', 'Maria']
# ---------------------------------------------------------------------------- #