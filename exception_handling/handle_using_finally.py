try:
    li =[10,20,30,40,50]
    print(li[10])
except IndexError:
    print("index is out of bounds.")
finally:
    print("This block is always executed.")