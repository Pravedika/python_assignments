try:
    result = 10 / 0
    print(result)
    li  = [10,20,30,40,50]
    print(li[10])
except ZeroDivisionError:  
    print("Error: Division by zero is not allowed.")  
except IndexError:
    print("index is out of bounds.")