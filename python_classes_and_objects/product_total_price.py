class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def total_price(self):
        return self.price * self.quantity

products = [
    Product("Pen", 10, 5),
    Product("Book", 50, 3),
    Product("Bag", 800, 2)
]

for product in products:
    print(product.name, product.total_price())
