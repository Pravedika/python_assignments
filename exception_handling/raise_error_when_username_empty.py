try:
    username = input("enter the username: ")
    if username == " ":
        raise ValueError("Enter valid username")
except ValueError as e:
    print("Error: ",e)