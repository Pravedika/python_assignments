class Book:
    def __init__(self, title):
        self.title = title

class Library:
    def __init__(self):
        self.books = [Book("Python"), Book("Java")]

    def display(self):
        for book in self.books:
            print(book.title)

Library().display()

print("Relationship: HAS-A")
