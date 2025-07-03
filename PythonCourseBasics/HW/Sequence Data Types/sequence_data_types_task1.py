# ---------------------------------- Task 1 ---------------------------------- #
# """ DESCRIPTION:
#     Write a program that asks the user to enter three numbers: start, stop, and step.
#     Create a range object using these values and convert it to a list named 'numbers'.

#     TIP: Use the range(start, stop, step) function and list() to convert it to a list.
# """

### Your code here

start_number = int(input("Enter start: "))
stop_number = int(input("Enter stop: "))
step_number = int(input("Enter step:"))
generated_list = list(range(start_number,stop_number,step_number)) 
print(f"Generated list: {generated_list}")

### EXPECTED OUTPUT:
# Enter start: 2
# Enter stop: 10
# Enter step: 2
# Generated list: [2, 4, 6, 8]
# ---------------------------------------------------------------------------- #
