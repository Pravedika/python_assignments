stored_username = "admin"
stored_password = "python"
username = input("Enter username: ")
password = input("Enter password: ")
valid = username == stored_username and password == stored_password
print("Login valid:", valid)
