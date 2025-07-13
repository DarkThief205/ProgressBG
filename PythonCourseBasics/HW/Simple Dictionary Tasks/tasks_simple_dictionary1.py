# ---------------------------------- Task 1 ---------------------------------- #
"""DESCRIPTION:
Create a dictionary to represent person's data:
    name      : Ivan
    age       : 30
    city      : Sofia


Print the data as shown:
"""
### YOUR CODE HERE
person = {
    'name': 'Ivan',
    'age': 30,
    'city': 'Sofia'
}

for key, value in person.items():
    print(f"{key:<10}: {value}")

### EXPECTED OUTPUT:
# name      : Ivan
# age       : 30
# city      : Sofia
# ---------------------------------------------------------------------------- #
