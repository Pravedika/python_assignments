class EmailService:
    def send_confirmation(self, email):
        print("Confirmation sent to:", email)

class Order:
    def __init__(self, order_id, email):
        self.order_id = order_id
        self.email = email

    def confirm(self, email_service):
        email_service.send_confirmation(self.email)

Order("ORD101", "user@example.com").confirm(EmailService())
