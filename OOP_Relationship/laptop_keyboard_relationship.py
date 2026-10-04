class Keyboard:
    def type(self):
        print("Keyboard is typing.")

class Laptop:
    def __init__(self):
        self.keyboard = Keyboard()

    def use(self):
        self.keyboard.type()

Laptop().use()

print("Relationship: HAS-A")
