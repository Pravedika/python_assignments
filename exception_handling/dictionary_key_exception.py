try:
    student= {"name":"praneeth",
              "age":12
              }
    key = input("Enter the key: ")
    print(student[key])
except KeyError:
    print("Invalid Key")