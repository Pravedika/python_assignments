try:
    li =[10,20,30,40,50]
    index = int(input("enter the index to get the value:"))
    print(li[index])
except IndexError:
    print("Invalid index is entered")