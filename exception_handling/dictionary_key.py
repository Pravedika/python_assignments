def search_key(data, key):
    try:
        print("Value:", data[key])
    except KeyError:
        print("Key not found")

student = {"name": "Ravi", "age": 20, "marks": 85}
search_key(student, "name")
search_key(student, "salary")
