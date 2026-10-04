class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Withdrawal successful")
        else:
            print("Insufficient balance")

account = BankAccount(5000)
account.withdraw(2000)
print("Balance:", account.balance)
account.withdraw(5000)
