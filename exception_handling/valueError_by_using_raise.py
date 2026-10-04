try:
    n = int(input("enter the value : "))
    if n < 0 :
        raise ValueError("please enter valid number")
except ValueError as e:
    print("Error: ",e)