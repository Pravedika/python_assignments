class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def total_cost(self):
        return self.price * self.quantity

product = Product("Keyboard", 800, 3)
print("Total Cost:", product.total_cost())
