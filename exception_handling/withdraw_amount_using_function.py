def withdraw():
 try:
    balance = 10000
    amount = float(input("enter the withdrawal amount: "))
    if amount <= 0:
        print("Invalid amount")
    if amount > balance:
        raise ValueError("Insufficient amount")
    balance = balance-amount
 except ValueError:
    print("Enter valid amount")