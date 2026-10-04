class InvalidUsernameError(Exception):
    pass
try:
    username = input("enter the username: ")
    if username != "admin":
        raise InvalidUsernameError("Invalid Username")
    print("Valid Username")
except InvalidUsernameError as e:
    print("Error: ",e)