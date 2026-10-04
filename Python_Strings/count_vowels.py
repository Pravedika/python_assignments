s1 = "pravedika"
s2 ="aeiou"
count = 0
for x in s1:
    if x in s2:
        count += 1
print("Number of vowels in the string:", count)