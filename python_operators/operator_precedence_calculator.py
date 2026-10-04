expression = input("Enter an arithmetic expression: ")
try:
    result = eval(expression, {"__builtins__": {}}, {})
    print("Result:", result)
except Exception:
    print("Invalid expression.")
