from abc import ABC, abstractmethod
import math

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        print("Rectangle area:", self.length * self.width)

    def perimeter(self):
        print("Rectangle perimeter:", 2 * (self.length + self.width))

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        print("Circle area:", math.pi * self.radius ** 2)

    def perimeter(self):
        print("Circle perimeter:", 2 * math.pi * self.radius)

Rectangle(10, 5).area()
Rectangle(10, 5).perimeter()
Circle(5).area()
Circle(5).perimeter()
