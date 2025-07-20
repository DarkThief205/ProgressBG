# ---------------------------------- Task 10 ---------------------------------- #
""" DESCRIPTION:
Create a function 'filter_words' that takes a list of words and a minimum length, and
returns a list of words that are longer than the given minimum length.
"""
def filter_words(words, min_length):
    result = []
    for word in words:
        if len(word) > min_length:
            result.append(word)
    return result

### EXPECTED OUTPUT:
# ['banana', 'cherry']
# ---------------------------------------------------------------------------- #
