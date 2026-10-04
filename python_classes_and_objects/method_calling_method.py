class Calculator:
    def add(self, a, b):
        return a + b

    def calculate_and_display(self, a, b):
        result = self.add(a, b)
        print("Result:", result)

calculator = Calculator()
calculator.calculate_and_display(10, 20)
