# ----------------------------------Task 1 ---------------------------------- #
### Description:
#  Ask the user for their name, age, and favorite color. Store this information
#  into variables and print a greeting in the console, for example:
#  "Hello, my name is Alice, I am 30 years old, and my favorite color is black."
#  Use f-strings and the variables to construct the message.

### Given:
# No initial variables are given. You need to get input from the user.


### Your code here:
user_name = input("Enter your name: ")
user_age = int(input("Enter your age: " ))
user_fav_color = input("Enter your favorite color: ")
print(f"Hello, my name is {user_name}, I am {user_age} years old, and my favorite color is {user_fav_color}.")

### Expected output (example):
# Enter your name: Alice
# Enter your age: 30
# Enter your favorite color: black
# Hello, my name is Alice, I am 30 years old, and my favorite color is black.
#-----------------------------------------------------------------------------#
