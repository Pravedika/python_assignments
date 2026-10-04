try:
    password = input("enter the password: ")
    if len(password) < 8:
     raise ValueError("Password must consists atleast 8 characters")
except ValueError as e:
    print("Error: ",e)