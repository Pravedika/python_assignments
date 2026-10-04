class Printer:
    def print(Self):
        print("Duck is walking")
class PDFPrinter:
    def print(Self):
        print("dog is walking")
def print_data(prints):
  prints.print()
p1 =Printer()
p2 = PDFPrinter()
print_data(p1)
print_data(p2)
