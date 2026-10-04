try:
    num = list(map(int,input("enter the list elements: ").split()))
    result = num[5]
except ValueError:
    print("Please enter valid integers")
except IndexError:
    print("you are accessing invalid index")
else:
    print(result)