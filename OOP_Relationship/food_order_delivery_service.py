class DeliveryService:
    def deliver(self, address):
        print("Food delivered to:", address)

class FoodOrder:
    def __init__(self, address):
        self.address = address

    def place_delivery(self, delivery_service):
        delivery_service.deliver(self.address)

FoodOrder("Main Street").place_delivery(DeliveryService())
