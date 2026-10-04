class Book:
    def display(self,title,author,price):
        print("Book title: ",title)
        print("Book Author: ",author)
        print("Book price: ",price)
b = Book()
b.display("The Book Thief","Markus Zusak",850)