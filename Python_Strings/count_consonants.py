s1 ="chandrika"
s2 ="aeiou"
count = 0
for x in s1:
    if x not in s2:
        count += 1
print("Number of consonants in the string:", count)