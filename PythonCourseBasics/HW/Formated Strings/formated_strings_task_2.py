# ---------------------------------- Task 2 ---------------------------------- #
### Description:
#  Ask the user for their birth year and the current year.
#  Calculate their age using these inputs, then print the result.

### Given:
# No initial variables are given. You need to get input from the user.

### Your code here:
user_birth_year = int(input("Enter birth year: ")) 
current_year = int(input("Enter the current year: "))
user_age = (current_year - user_birth_year)
print(f"You are {user_age} years old.")
### Expected output (example):
# Enter your birth year: 1995
# Enter the current year: 2025
# You are 30 years old.
#-----------------------------------------------------------------------------#
