try:
    a = int(input("Enter a number:"))
    square = a ** 2
except ValueError:
    print("Error: Please enter a valid integer.")
else:
    print("The square of the number is:",square)