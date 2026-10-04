from abc import ABC, abstractmethod

class BankAccount(ABC):
    def __init__(self, account_holder, account_number):
        self.account_holder = account_holder
        self.account_number = account_number

    @abstractmethod
    def calculate_interest(self):
        pass

class SavingsAccount(BankAccount):
    def calculate_interest(self):
        print("Account Holder:", self.account_holder)
        print("Account Number:", self.account_number)
        print("Interest: 4%")

SavingsAccount("Ravi", "ACC101").calculate_interest()
