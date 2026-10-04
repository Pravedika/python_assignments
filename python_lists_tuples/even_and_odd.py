numbers = [1, 2, 3, 4, 5]
even = [num % 2 == 0 for num in numbers]
print(even)
odd = [num % 2 !=  0 for num in numbers]
print(odd)