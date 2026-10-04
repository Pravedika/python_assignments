words = {
    "python": "A programming language",
    "list": "An ordered collection",
    "set": "An unordered collection of unique values",
    "dictionary": "A collection of key-value pairs"
}

word = input("Enter a word: ").lower()

if word in words:
    print("Meaning:", words[word])
else:
    print("Word not found")
