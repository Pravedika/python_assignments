products = {
    "Laptop": 55000,
    "Mouse": 800,
    "Keyboard": 1500,
    "Monitor": 12000,
    "Headphones": 900
}

for product, price in products.items():
    if price > 1000:
        print(product, price)
