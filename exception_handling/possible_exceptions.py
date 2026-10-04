try:
    a =int(input("enter the first value:  "))
    b = int(input("enter the second value: "))
    if b == 0:
        raise ZeroDivisionError("Division by zero is not allowed")
except ValueError:
    print("Please enter valid integers")
except ZeroDivisionError as e:
    print("Error: ",e)