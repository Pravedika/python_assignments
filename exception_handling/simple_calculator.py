try:
    a = int(input("Enter a number:"))
    b = int(input("Enter another number:"))
    result1 = a + b
    result2 = a - b
    result3 = a * b
    result4 = a / b
except ValueError:
    print("Error: Please enter valid integers.")
else:
    print("Addition:",result1)
    print("Subtraction: ",result2)
    print("Multiplication: ",result3)
    print("Division: ",result4)