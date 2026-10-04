class InvalidPasswordError(Exception):
    pass
try:
    password = input("enter the password: ")
    if password != "admin@123":
        raise InvalidPasswordError("Invalid Password")
    print("Valid Password")
except InvalidPasswordError as e:
    print("Error: ",e)