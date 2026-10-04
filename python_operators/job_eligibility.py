age = int(input("Enter age: "))
qualification = input("Enter qualification: ").strip().lower()
eligible = age >= 18 and qualification == "degree"
print("Job eligible:", eligible)
