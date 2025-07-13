# ---------------------------------- Task 4 ---------------------------------- #
""" DESCRIPTION:
    Given a dictionary, remove a key-value pair and print the updated dictionary.
"""

### Your code here
person = {
    'name': 'Ivan',
    'age': 31,
    'city': 'Sofia'
}

person.pop('age')
print(person)

### EXPECTED OUTPUT:
# {'name': 'Ivan', 'city': 'Sofia'}
# ---------------------------------------------------------------------------- #
