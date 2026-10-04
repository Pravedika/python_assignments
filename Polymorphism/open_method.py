class PDF:
    def open(self):
        print("Opening PDF file")
class Word:
    def open(self):
        print("Opening Word file")
class Excel:
    def open(self):
        print("Opening Excel file")
p =PDF()
w =Word()
e =Excel()
p.open()
w.open()
e.open()