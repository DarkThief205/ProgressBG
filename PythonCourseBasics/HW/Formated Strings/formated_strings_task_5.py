# ---------------------------------- Task 5 ---------------------------------- #
### Description:
#  Ask the user for the current temperature in Celsius.
#  Convert this temperature to Fahrenheit using the formula: $F = (C \times 9/5) + 32$.
#  Print both the Celsius and Fahrenheit temperatures, formatted to one decimal place,
#  using an f-string.

### Given:
# No initial variables are given. You need to get input from the user.

### Your code here:

temp_celsius = float(input("Enter temperature in Celsius:"))
temp_fahrenheit = (temp_celsius * 9/5) + 32
print(f"{temp_celsius}°C is equal to {temp_fahrenheit}°F")

### Expected output (example):
# Enter temperature in Celsius: 25
# 25.0°C is equal to 77.0°F
#-----------------------------------------------------------------------------#