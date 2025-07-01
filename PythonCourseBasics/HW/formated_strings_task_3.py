# ---------------------------------- Task 3 ---------------------------------- #
### Description:
#  Ask the user to enter a large numeric amount (e.g., 1234567.89).
#  Format this number to be displayed as a USD currency with two decimal places and
#  commas for thousands separators. Example: "$1,234,567.89".
#  Use an f-string to format and print the result.

### Given:
# No initial variables are given. You need to get input from the user.

### Your code here:
money_amount = float(input("Enter an amount: "))
print(f"${money_amount:,.2f}")

### Expected output (example):
# Enter an amount: 1234567.89
# $1,234,567.89
# -------------------------------------------------------------------- #