# ---------------------------------- Task 4 ---------------------------------- #
### Description:
#  Ask the user for the names and prices of three different shopping items.
#  Create a simple receipt format. Use f-strings to format each item name
#  aligned to the left and its price aligned to the right.
#  Each line for an item should be 30 characters wide.

### Given:
# No initial variables are given. You need to get input from the user.

### Your code here:

item1 = input("Enter name of item 1: ")
price1 = float(input("Enter price of item 1: "))
item2 = input("Enter name of item 2: ")
price2 = float(input("Enter price of item 2: "))
item3 = input("Enter name of item 3: ")
price3 = float(input("Enter price of item 3: "))

print(f"{'Shopping Items':>30}")
print(f"{item1:<30}{price1:>10.2f}")
print(f"{item2:<30}{price2:>10.2f}")
print(f"{item3:<30}{price3:>10.2f}")

### Expected output (example):
# Enter name of item 1: Milk
# Enter price of item 1: 1.99
# Enter name of item 2: Bread
# Enter price of item 2: 2.49
# Enter name of item 3: Eggs
# Enter price of item 3: 3.59
#
#           Shopping Items:
# Milk                          1.99
# Bread                         2.49
# Eggs                          3.59
#-----------------------------------------------------------------------------#