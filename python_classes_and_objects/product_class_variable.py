class Product:
    category = "Electronics"

    def __init__(self, name, price):
        self.name = name
        self.price = price

products = [Product("Mobile", 20000), Product("Laptop", 60000)]

for product in products:
    print(product.name, product.price, product.category)
