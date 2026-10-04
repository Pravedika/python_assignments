class InvalidTransactionError(Exception):
    pass
try:
    balance = 9000
    amount = float(input("enter the withdrwal amount: "))
    if amount <= 0:
       raise InvalidTransactionError("invalid amount")
    if amount > balance:
       raise InvalidTransactionError("Insufficient Balance")
    print("Transaction Successful!")
except InvalidTransactionError as e:
    print("Error: ",e)
    
   