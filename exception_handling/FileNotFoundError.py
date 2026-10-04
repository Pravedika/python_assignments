try:
    with open("student.txt","r") as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print("The specified file was not found.")