while True:
    print("\nOperator Calculator")
    print("1. Arithmetic")
    print("2. Assignment")
    print("3. Comparison")
    print("4. Logical")
    print("5. Membership")
    print("6. Identity")
    print("7. Bitwise")
    print("8. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        print("Addition:", a + b)
        print("Subtraction:", a - b)
        print("Multiplication:", a * b)
        if b != 0:
            print("Division:", a / b)
            print("Floor division:", a // b)
            print("Modulus:", a % b)
        print("Power:", a ** b)

    elif choice == "2":
        value = float(input("Enter value: "))
        value += 5
        value *= 2
        value -= 3
        print("After assignment operations:", value)

    elif choice == "3":
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        print("Equal:", a == b)
        print("Not equal:", a != b)
        print("Greater:", a > b)
        print("Less:", a < b)

    elif choice == "4":
        a = int(input("Enter first boolean value (0/1): "))
        b = int(input("Enter second boolean value (0/1): "))
        print("AND:", bool(a) and bool(b))
        print("OR:", bool(a) or bool(b))
        print("NOT first:", not bool(a))

    elif choice == "5":
        items = ["Python", "SQL", "HTML"]
        item = input("Enter item to search: ")
        print("Exists:", item in items)

    elif choice == "6":
        first = []
        second = first
        print("Same object:", first is second)
        print("Different object:", first is not [])

    elif choice == "7":
        a = int(input("Enter first integer: "))
        b = int(input("Enter second integer: "))
        print("AND:", a & b)
        print("OR:", a | b)
        print("XOR:", a ^ b)
        print("NOT first:", ~a)
        print("Left shift first:", a << 1)
        print("Right shift first:", a >> 1)

    elif choice == "8":
        print("Exiting calculator.")
        break

    else:
        print("Invalid choice.")
