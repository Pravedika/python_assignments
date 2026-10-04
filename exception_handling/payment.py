class InvalidPaymentError(Exception):
    pass

class Payment:
    def pay(self, amount):
        try:
            if amount <= 0:
                raise InvalidPaymentError(
                    "Payment amount must be greater than zero"
                )

            print("Payment successful")
            print("Amount paid:", amount)
        except InvalidPaymentError as e:
            print("Error:", e)

payment = Payment()
payment.pay(1000)
payment.pay(-500)
