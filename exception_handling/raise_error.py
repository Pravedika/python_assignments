try:
    balance = 5000
    amount = float(input("enter the amount: "))
    if amount > balance:
        raise ValueError("Insufficient Balance")
except ValueError as e:
    print("Error: ",e)
else:
    print("Transaction completed successfully")