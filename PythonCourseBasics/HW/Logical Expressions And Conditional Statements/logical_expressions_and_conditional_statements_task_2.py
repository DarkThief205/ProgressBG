# ---------------------------------- Task 2 ---------------------------------- #
# """ DESCRIPTION:
#     Write a program to check whether a year input by the user is a leap year or not. Use the rule for Gregorian calendar:
#     Every year that is exactly divisible by four is a leap year, except for years that are exactly divisible by 100, but these centurial years are leap years if they are exactly divisible by 400.
#     For example, the years 1700, 1800, and 1900 are not leap years, but the years 1600 and 2000 are.
# """

### Your code here

year = int(input("Enter a year: "))

if year % 400 == 0:
    print(f"{year} is a leap year.")
elif year % 100 == 0:
    print(f"{year} is not a leap year.")
elif year % 4 == 0:
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")

### EXPECTED OUTPUT:
# Enter a year: 2024
# 2024 is a leap year

# Enter a year: 2050
# 2050 is not leap year.

# -------------------------------------------------------------------------- #
