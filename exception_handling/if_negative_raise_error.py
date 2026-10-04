try:
    a = int(input("enter the number: "))
    if a < 0:
        raise ValueError("Enter only positive numbers")
except ValueError as e:
    print("Error: ",e)