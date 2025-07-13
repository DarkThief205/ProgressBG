
# ---------------------------------- Task 7 ---------------------------------- #
""" DESCRIPTION:
    Given a dictionary, print all key-value pairs in the format "key: value".
"""

### Your code here
person = {
    'name': 'Ivan',
    'age': 30,
    'city': 'Sofia'
}

# Print key-value pairs
for key, value in person.items():
    print(f"{key}: {value}")
    
### EXPECTED OUTPUT:
# name: Ivan
# age: 30
# city: Sofia
# ---------------------------------------------------------------------------- #
