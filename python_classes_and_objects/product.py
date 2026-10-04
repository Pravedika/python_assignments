class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

product = Product("Keyboard", 800, 2)
print("Product:", product.name)
print("Price:", product.price)
print("Quantity:", product.quantity)
