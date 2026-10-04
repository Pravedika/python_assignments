age = int(input("Enter age: "))
membership = input("Are you a member? ").strip().lower()
eligible = age >= 60 or membership == "yes"
print("Eligible for discount:", eligible)
