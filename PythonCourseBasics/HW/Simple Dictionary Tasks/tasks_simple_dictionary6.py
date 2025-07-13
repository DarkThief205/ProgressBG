# ---------------------------------- Task 6 ---------------------------------- #
""" DESCRIPTION:
    Given two dictionaries, merge them into one and print the result.
"""
### Your code here
person = {
    'name': 'Ivan',
    'age': 30,
    'city': 'Sofia',
    'job': 'Developer'
}

extra_info = {
    'salary': 50000
}

# Merge dictionaries
person.update(extra_info)

print(person)

### EXPECTED OUTPUT:
# {'name': 'Ivan', 'age': 30, 'city': 'Sofia', 'job': 'Developer', 'salary': 50000}

# ---------------------------------------------------------------------------- #
