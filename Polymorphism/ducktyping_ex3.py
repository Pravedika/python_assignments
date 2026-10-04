class Printer:
    def prints(self):
        print("Printer used to take prints from data")
class PDFPrinter:
    def prints(self):
        print("PDFPrinter is used to take pdf prints from data")
def show(p):
    p.prints()
p1=Printer()
p2=PDFPrinter()
show(p1)
show(p2)
