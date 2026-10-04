from abc import ABC, abstractmethod

class Delivery(ABC):
    @abstractmethod
    def calculate_charge(self):
        pass

    @abstractmethod
    def deliver(self):
        pass

class StandardDelivery(Delivery):
    def calculate_charge(self):
        return 50

    def deliver(self):
        print("Standard delivery charge:", self.calculate_charge())

class ExpressDelivery(Delivery):
    def calculate_charge(self):
        return 100

    def deliver(self):
        print("Express delivery charge:", self.calculate_charge())

StandardDelivery().deliver()
ExpressDelivery().deliver()
