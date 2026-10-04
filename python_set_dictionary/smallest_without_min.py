numbers = {12, 45, 7, 89, 23, 56}

smallest = None

for num in numbers:
    if smallest is None or num < smallest:
        smallest = num

print("Smallest:", smallest)
