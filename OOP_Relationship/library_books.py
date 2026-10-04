class Book:
    def __init__(self, title):
        self.title = title

class Library:
    def __init__(self):
        self.books = [
            Book("Python Basics"),
            Book("Java Programming"),
            Book("SQL Guide")
        ]

    def display_books(self):
        for book in self.books:
            print("Book:", book.title)

Library().display_books()
