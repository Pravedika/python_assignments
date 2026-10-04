username = input("Enter username: ").strip()
password = input("Enter password: ")
registered_users = ["ravi", "priya", "anvesh"]

valid_username = username != "" and username not in registered_users
valid_password = len(password) >= 6 and " " not in password

print("Username valid:", valid_username)
print("Password valid:", valid_password)
print("Registration valid:", valid_username and valid_password)
