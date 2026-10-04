class InvalidProductError(Exception):
    pass

class InvalidQuantityError(Exception):
    pass

class ShoppingCart:
    def __init__(self):
        self.products = {
            "Laptop": 50000,
            "Mouse": 500,
            "Keyboard": 1000
        }

    def add_product(self, product, quantity):
        try:
            if product not in self.products:
                raise InvalidProductError("Product does not exist")

            if quantity <= 0:
                raise InvalidQuantityError(
                    "Quantity must be greater than zero"
                )

            total = self.products[product] * quantity
            print("Product:", product)
            print("Quantity:", quantity)
            print("Total:", total)
        except InvalidProductError as e:
            print("Error:", e)
        except InvalidQuantityError as e:
            print("Error:", e)

cart = ShoppingCart()
cart.add_product("Laptop", 2)
cart.add_product("Mobile", 1)
cart.add_product("Mouse", -2)
