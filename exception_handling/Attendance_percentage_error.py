try:
    n = int(input("Enter the percentage: "))
    if n <= 75:
        raise ValueError("Attendance Must greater than 75%")
except ValueError as e:
    print("Error: ",e)