try:
    a =float(input("Enter a number: "))
    b = 10/0
except ValueError:
    print("Please enter the valid number")
except ZeroDivisionError:
    print("Division by zero is not allowed.")