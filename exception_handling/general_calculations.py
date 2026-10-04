try:
    a = int(input("enter the first value: "))
    b = int(input("enter the second value: "))
    if b == 0:
        raise ZeroDivisionError("Division By Zero is not allowed")
except ZeroDivisionError as e:
    print("Error: ",e)
else:
    print("sum=",a+b)
    print("subtract=",a-b)
    print("Product=",a*b)
    print("Division=",a/b)