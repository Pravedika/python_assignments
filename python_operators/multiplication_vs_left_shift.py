number = int(input("Enter a number: "))
shift = int(input("Enter shift count: "))
multiplication_result = number * (2 ** shift)
left_shift_result = number << shift
print("Multiplication result:", multiplication_result)
print("Left shift result:", left_shift_result)
