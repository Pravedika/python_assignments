numbers = {
    "a": 10,
    "b": 15,
    "c": 20,
    "d": 7,
    "e": 12
}

even_count = 0
odd_count = 0

for value in numbers.values():
    if value % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

print("Even values:", even_count)
print("Odd values:", odd_count)
