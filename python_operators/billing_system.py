total = 0
items = int(input("Enter number of items: "))

for _ in range(items):
    price = float(input("Enter item price: "))
    quantity = int(input("Enter quantity: "))
    total += price * quantity

discount = 0
if total >= 5000:
    discount = 10
elif total >= 3000:
    discount = 5

discount_amount = total * discount / 100
final_bill = total - discount_amount

print("Subtotal:", total)
print("Discount:", discount, "%")
print("Final bill:", final_bill)
