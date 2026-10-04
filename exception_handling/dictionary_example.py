student = {
    "name": "Ravi",
    "age": 20,
    "marks": 85
}
try:
    key = input("Enter dictionary key: ")
    if key == "":
        raise ValueError("Key cannot be empty")
    print("Value:", student[key])
except ValueError as e:
    print("Invalid input:", e)
except KeyError:
    print("Key does not exist")