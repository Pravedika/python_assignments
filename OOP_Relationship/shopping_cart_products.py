class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class ShoppingCart:
    def __init__(self):
        self.products = [
            Product("Laptop", 50000),
            Product("Mouse", 1000),
            Product("Keyboard", 2000)
        ]

    def display_cart(self):
        for product in self.products:
            print(product.name, "-", product.price)

ShoppingCart().display_cart()
