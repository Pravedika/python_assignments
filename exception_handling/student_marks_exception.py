try:
    marks = int(input("enter the marks: "))
    if marks < 100 and marks > 0:
        raise ValueError("please enter valid integer")
except ValueError as e:
    print("Error: ",e)