products = {
    "Laptop": 55000,
    "Mouse": 800,
    "Mobile": 18000,
    "Keyboard": 1500,
    "Monitor": 12000
}

expensive_products = set()

for product, price in products.items():
    if price > 5000:
        expensive_products.add(product)

print(expensive_products)
