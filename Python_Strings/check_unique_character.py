s = "python"
unique = True
for ch in s:
    if s.count(ch) > 1:
        unique = False
        break
if unique:
    print("String contains unique characters")
else:
    print("String does not contain unique characters")