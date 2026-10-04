class BookUnavailableError(Exception):
    pass

class Library:
    def __init__(self):
        self.books = ["Python", "Java", "SQL"]

    def borrow_book(self, book):
        try:
            if book not in self.books:
                raise BookUnavailableError("Book is not available")

            self.books.remove(book)
            print(book, "borrowed successfully")
        except BookUnavailableError as e:
            print("Error:", e)

library = Library()
library.borrow_book("Python")
library.borrow_book("C++")
