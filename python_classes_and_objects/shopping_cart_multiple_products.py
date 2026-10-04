class ShoppingCart:
    def __init__(self):
        self.products = []

    def add_product(self, name, price, quantity):
        self.products.append({
            "name": name,
            "price": price,
            "quantity": quantity
        })

    def calculate_total(self):
        return sum(product["price"] * product["quantity"] for product in self.products)

cart = ShoppingCart()
cart.add_product("Book", 500, 2)
cart.add_product("Pen", 20, 5)
cart.add_product("Bag", 800, 1)

print("Total Bill:", cart.calculate_total())
