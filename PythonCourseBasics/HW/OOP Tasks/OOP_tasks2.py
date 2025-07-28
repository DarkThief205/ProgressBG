# ---------------------------------- Task 2 ---------------------------------- #
""" DESCRIPTION:
Create a class called 'Student' to represent a student. The class should have the following attributes and methods:

Attributes:
- 'name': a string representing the student's name.
- 'student_id': an integer representing the student's ID.
- 'courses': a list representing the courses the student is enrolled in.

Methods:
- 'add_course(course_name)': a method that adds a course to the student's list of courses.
- 'remove_course(course_name)': a method that removes a course from the student's list of courses.
- 'list_courses()': a method that prints the list of courses the student is enrolled in.

Create an instance of the 'Student' class with your own information and demonstrate the usage of the methods.


"""

class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        self.courses = []  

    def add_course(self, course_name):
        if course_name not in self.courses:
            self.courses.append(course_name)

    def remove_course(self, course_name):
        if course_name in self.courses:
            self.courses.remove(course_name)
        

    def list_courses(self):
        if self.courses:
            print("Courses:", ",".join(self.courses))
        


### TEST
student1 = Student("Alice", 12345)
student1.add_course("Math")
student1.add_course("History")
student1.list_courses()

### EXPECTED OUTPUT:
# Courses: Math,History
# ---------------------------------------------------------------------------- #
