try:
    number1 = int(input("Enter first number: "))
    number2 = int(input("Enter second number: "))
    result = number1 / number2
    numbers = [10, 20, 30]
    index = int(input("Enter index: "))
    print("Division result:", result)
    print("List value:", numbers[index])
except ValueError:
    print("Please enter numbers only")
except ZeroDivisionError:
    print("Cannot divide by zero")
except IndexError:
    print("Index is out of range")
except Exception as e:
    print("Some other error occurred:", e)