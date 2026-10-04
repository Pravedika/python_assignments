def access_element(numbers, index):
    try:
        print("Element:", numbers[index])
    except IndexError:
        print("Index is out of range")

numbers = [10, 20, 30, 40]
access_element(numbers, 2)
access_element(numbers, 10)
