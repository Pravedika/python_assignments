numbers = {12, 45, 7, 89, 23, 56}

largest = None

for num in numbers:
    if largest is None or num > largest:
        largest = num

print("Largest:", largest)
