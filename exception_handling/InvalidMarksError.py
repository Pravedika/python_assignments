class InvalidMarksError(Exception):
    pass
try:
    marks =int(input("enter the marks: "))
    if marks < 35:
        raise InvalidMarksError("marks must be greater than 35")
    print("Student passed")
except InvalidMarksError as e:
    print("Error: ",e) 