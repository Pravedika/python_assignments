amount = float(input("Enter shopping amount: "))
member = input("Are you a member? ").strip().lower()
discount = 0
if amount >= 5000 and member == "yes":
    discount = 20
elif amount >= 3000 or member == "yes":
    discount = 10
discount_amount = amount * discount / 100
final_amount = amount - discount_amount
print("Discount:", discount, "%")
print("Final amount:", final_amount)
