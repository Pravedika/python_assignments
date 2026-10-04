s1 = input("Enter a string: ")
words = s1.split()
reverse_words = words[::-1]
print("The reverse order of words in the string is:", " ".join(reverse_words))