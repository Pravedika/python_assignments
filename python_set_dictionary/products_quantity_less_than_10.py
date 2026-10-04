products = {
    "Pens": 25,
    "Books": 7,
    "Bags": 12,
    "Pencils": 5
}

for product, quantity in products.items():
    if quantity < 10:
        print(product, quantity)
