try:
    with open("example.txt", "r") as file:
        content = file.read()
except FileNotFoundError:
    print("The specified file was not found.")
else:
    print(content)
finally:
    print("This block is always executed.")