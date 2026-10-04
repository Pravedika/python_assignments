from abc import ABC, abstractmethod

class BankAccount(ABC):
    @abstractmethod
    def calculate_interest(self):
        pass

class SavingsAccount(BankAccount):
    def calculate_interest(self):
        print("Savings Account interest: 4%")

class CurrentAccount(BankAccount):
    def calculate_interest(self):
        print("Current Account interest: 2%")

SavingsAccount().calculate_interest()
CurrentAccount().calculate_interest()
