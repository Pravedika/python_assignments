class InvalidAgeError(Exception):
    pass
try:
    balance = float(input("enter the balance amount: "))
    amount = float(input("enter the amount: "))
    if balance < amount:
        raise InvalidAgeError("Insufficient balance")
    print("Sufficient balance")
except InvalidAgeError as e:
    print("Error: ",e)

