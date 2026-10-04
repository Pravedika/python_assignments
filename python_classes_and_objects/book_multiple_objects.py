class Book:
    def __init__(self, title, author, price, pages):
        self.title = title
        self.author = author
        self.price = price
        self.pages = pages

books = [
    Book("Python", "John", 500, 300),
    Book("Java", "Smith", 600, 400),
    Book("SQL", "David", 450, 250)
]

for book in books:
    print(book.title, book.author, book.price, book.pages)
