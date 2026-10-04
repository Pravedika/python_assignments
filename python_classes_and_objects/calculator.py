class Calculator:
    def addition(self, a, b):
        return a + b

    def subtraction(self, a, b):
        return a - b

    def multiplication(self, a, b):
        return a * b

    def division(self, a, b):
        return a / b

calculator = Calculator()
print("Addition:", calculator.addition(10, 5))
print("Subtraction:", calculator.subtraction(10, 5))
print("Multiplication:", calculator.multiplication(10, 5))
print("Division:", calculator.division(10, 5))
