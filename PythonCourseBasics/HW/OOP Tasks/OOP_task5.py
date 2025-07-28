# ---------------------------------- Task 5 ---------------------------------- #
""" DESCRIPTION:
Create a base class called 'Shape' to represent a geometric shape. The class should have the following attributes and methods:

Attributes:
- 'name': a string representing the name of the shape.

Methods:
- 'area()': a method that will return the string 'Not implemented for common shape'

Create two subclasses, 'Rectangle' and 'Circle', that inherit from the 'Shape' class and implement their specific area calculation methods.

Demonstrate the usage of the 'Rectangle' and 'Circle' classes by creating instances of each and calculating their respective areas.

"""
import math

### Define the Shape base class
class Shape:
    def __init__(self, name):
        self.name = name

    def area(self):
        return "Not implemented for common shape"
### Define the Rectangle class inheriting from Shape
class Rectangle(Shape):
    def __init__(self, name, width, height):
        super().__init__(name) #Super() calls __init__ from Shape
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

### Define the Circle class inheriting from Shape
class Circle(Shape):
    def __init__(self, name, radius):
        super().__init__(name)
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

### TEST:
rectangle1 = Rectangle("Rectangle", 5.0, 3.0)
circle1 = Circle("Circle", 2.0)
print(rectangle1.area())
print(f"{circle1.area():.2f}")

### EXPECTED OUTPUT:
# 15.0
# 12.57
# ---------------------------------------------------------------------------- #
