try:
    a = int(input("Enter a number: "))
    b = int(input("Enter another number: "))
except ValueError:
    print("Error: Please enter valid integers.")