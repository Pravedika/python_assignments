try:
    employee = {"name":"sirish",
                "role":"IT",
                "salary":50000}
    key = input("enter the key: ")
    print(employee[key])
except KeyError:
    print("key doesn't specified in dictionary")