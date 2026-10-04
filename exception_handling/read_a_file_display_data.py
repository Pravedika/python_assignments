try:
    with open("course.txt") as file:
        content = file.read()
except FileNotFoundError:
    print("File was not found in")
else:
    print(content)