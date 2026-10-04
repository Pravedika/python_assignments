class BankAccount:
    def deposit(self, amount):
        print("Deposited:", amount)

class SavingsAccount(BankAccount):
    def calculate_interest(self):
        print("Savings interest is calculated.")

class CurrentAccount(BankAccount):
    def calculate_interest(self):
        print("Current account interest is calculated.")

SavingsAccount().deposit(5000)
SavingsAccount().calculate_interest()
CurrentAccount().deposit(10000)
CurrentAccount().calculate_interest()
