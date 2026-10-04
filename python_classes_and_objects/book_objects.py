class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

book_one = Book("Python Basics", "John", 450)
book_two = Book("Django Guide", "David", 600)

for book in [book_one, book_two]:
    print("Title:", book.title)
    print("Author:", book.author)
    print("Price:", book.price)
    print()
