try:
    student = {"name" :"veda",
               "age": 17,
               "course" :"python-fullstack"}
    key = input("enter the key:")
    print(student[key])
except KeyError:
    print("The key is doesn't exist in dictionary")
