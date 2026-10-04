s1 ="python is a programming language"
count = 0
for x in s1:
    if x.isspace():
        count += 1
print("Number of spaces in the string:", count)