class Shape:
    def display(self):
        print("This is a shape.")

class Rectangle(Shape):
    def calculate_area(self, length, width):
        print("Area:", length * width)

rectangle = Rectangle()
rectangle.display()
rectangle.calculate_area(10, 5)
