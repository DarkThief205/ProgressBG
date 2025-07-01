# ---------------------------------- Task 3 ---------------------------------- #
# """ DESCRIPTION:
#     Develop a simple temperature converter program that converts temperatures from Fahrenheit to Celsius and vice versa based on user choice. Make a user-friendly interface as given in EXPECTED OUTPUT:.

#     Temperature conversions use the following formulas:
#     Temperature in degrees Fahrenheit (°F) = (Temperature in degrees Celsius (°C) * 9/5) + 32.
#     Temperature in degrees Celsius (°C) = (Temperature in degrees Fahrenheit (°F) - 32) * 5/9.
# """

### Your code here

print(f"""{'*'*10}Fahrenheit/Celsius Converter{'*'*10}
# 1 => Convert to Fahrenheit                     
# 2 => Convert to Celsius                        
{'*'*50}""")

user_choice = int(input("Enter your choice [1/2]: "))

if user_choice == 1:
    temperature_celsius = float(input("Enter temperature in C: "))
    temperature_convert_fahrenheit = (temperature_celsius * 9/5) + 32
    print(f"{temperature_celsius}C = {temperature_convert_fahrenheit}F")
elif user_choice == 2:
    temperature_fahrenheit = float(input("Enter temperature in F: ")) 
    temperature_convert_celsius = (temperature_fahrenheit - 32) * 5/9
    print(f"{temperature_fahrenheit}F = {temperature_convert_celsius}C")
else:
    print("Choose a number between [1/2].")

### EXPECTED OUTPUT:
# **********Fahrenheit/Celsius Converter ***********
# # 1 => Convert to Fahrenheit                     #
# # 2 => Convert to Celsius                        #
# **************************************************
# Enter your choice [1/2]: 1
# Enter temperature in C: 20
# 20.0C = 68.0F

# -------------------------------------------------------------------------- #
