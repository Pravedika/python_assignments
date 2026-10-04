try:
    a =10/0
    print(a)
except ZeroDivisionError:
    print("Division by Zero is not allowed")
finally:
    print("finally block is always executedd..")