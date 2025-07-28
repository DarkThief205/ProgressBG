# ---------------------------------- Task 3 ---------------------------------- #
""" DESCRIPTION:
Create a class called 'Book' to represent a book in a library system. The class should have the following attributes and methods:

Attributes:
- 'title': a string representing the title of the book.
- 'author': a string representing the author of the book.
- 'isbn': a string representing the ISBN of the book.
- 'year': an integer representing the publication year of the book.

Methods:
- '__str__()': a method that returns a formatted string with the book's title, author, ISBN, and publication year.

Create a class called 'Library' that manages a collection of books. The class should have the following methods:

Methods:
- 'add_book(book)': adds a book to the library's collection.
- 'remove_book(isbn)': removes a book from the library by its ISBN.
- 'find_book(isbn)': finds and returns a book by its ISBN. If not found, returns None.
- 'list_books()': prints a list of all books in the library.

Create instances of the 'Book' class and demonstrate the usage of the 'Library' class by adding, removing, and listing books.
"""


### Define the Book class


### Define the Library class


### TEST
# book1 = Book("1984", "George Orwell", "123456789", 1949)
# book2 = Book("To Kill a Mockingbird", "Harper Lee", "987654321", 1960)

# library = Library()
# library.add_book(book1)
# library.add_book(book2)

# print("List of books in the library:")
# library.list_books()

# # Remove a book
# library.remove_book("123456789")
# print("\nList of books after removal:")
# library.list_books()

# # Find a book
# book = library.find_book("987654321")
# if book:
#     print(f"\nFound book: {book}")
# else:
#     print("\nBook not found.")


### EXPECTED OUTPUT:
# List of books in the library:
# Title: 1984
# Author: George Orwell
# ISBN: 123456789
# Year: 1949
# --------------------
# Title: To Kill a Mockingbird
# Author: Harper Lee
# ISBN: 987654321
# Year: 1960
# --------------------

# List of books after removal:
# Title: To Kill a Mockingbird
# Author: Harper Lee
# ISBN: 987654321
# Year: 1960
# --------------------

# Found book: Title: To Kill a Mockingbird
# Author: Harper Lee
# ISBN: 987654321
# Year: 1960
# ---------------------------------------------------------------------------- #
