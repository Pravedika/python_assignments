try:
    student ={ "name": "veda", "age": 17 }
    print(student["gender"])
except KeyError:
    print("The specified key does not exist in the dictionary.")