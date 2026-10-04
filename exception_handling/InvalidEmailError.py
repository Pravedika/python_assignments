class InvalidEmailError(Exception):
    pass
try:
    email = input("enter the email: ")
    if email != "admin123@gmail.com":
        raise InvalidEmailError("Invalid Email")
    print("Valid Email")
except InvalidEmailError as e:
    print("Error: ",e)