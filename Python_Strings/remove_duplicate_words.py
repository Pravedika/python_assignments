sentence = "python is easy and python is powerful"
words = sentence.split()
duplicates = []
for word in words:
    if words.count(word) > 1 and word not in duplicates:
        duplicates.append(word)
print(duplicates)