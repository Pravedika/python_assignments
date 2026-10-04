class ShoppingCart:
    def __init__(self):
        self.products = []

    def add_product(self, name, price):
        self.products.append({"name": name, "price": price})

    def remove_product(self, name):
        self.products = [product for product in self.products if product["name"] != name]

    def calculate_total(self):
        return sum(product["price"] for product in self.products)

cart = ShoppingCart()
cart.add_product("Book", 500)
cart.add_product("Pen", 20)
cart.add_product("Bag", 800)
cart.remove_product("Pen")
print("Total:", cart.calculate_total())
