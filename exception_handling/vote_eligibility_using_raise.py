try:
    age = int(input("enter the age: "))
    if age < 18:
        raise ValueError("Age must be greater than 18")
except ValueError as e:
    print("Error: ",e)
else:
    print("eligibile to vote")