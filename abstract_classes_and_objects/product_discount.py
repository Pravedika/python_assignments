from abc import ABC, abstractmethod

class Product(ABC):
    def __init__(self, product_name, price):
        self.product_name = product_name
        self.price = price

    @abstractmethod
    def calculate_discount(self):
        pass

class Electronics(Product):
    def calculate_discount(self):
        discount = self.price * 0.10
        print("Product:", self.product_name)
        print("Discount:", discount)
        print("Final Price:", self.price - discount)

Electronics("Laptop", 50000).calculate_discount()
