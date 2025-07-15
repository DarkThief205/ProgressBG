# ---------------------------------- Task 1 ---------------------------------- #
"""DESCRIPTION:
Write a function named 'calculate_area' that takes two parameters (length and width)
and returns the area of a rectangle.
"""


### YOUR CODE HERE
lenght = int(input("Enter lenght of the rectangle: "))
width = int(input("Enter lenght of the rectangle: "))
def calculate_area(lenght, width):
    area_calcuation = lenght * width
    print(area_calcuation)

calculate_area(lenght,width)
### TEST:
# print(calculate_area(10, 5))

### EXPECTED OUTPUT:
# 50

# ---------------------------------------------------------------------------- #
