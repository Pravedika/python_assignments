class LibraryBook:
    def __init__(self, title):
        self.title = title
        self.issued = False

    def issue(self):
        if not self.issued:
            self.issued = True
            print("Book issued")
        else:
            print("Book is already issued")

    def return_book(self):
        if self.issued:
            self.issued = False
            print("Book returned")
        else:
            print("Book was not issued")

book = LibraryBook("Python Basics")
book.issue()
book.return_book()
