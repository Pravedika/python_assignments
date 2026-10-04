s1 ="abc34123as1"
count = 0
for x in s1:
    if x.isdigit():
        count += 1
print("Number of digits in the string:", count)