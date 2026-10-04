class StringOperations:
    def __init__(self, text):
        self.text = text

    def reverse(self):
        return self.text[::-1]

    def count_vowels(self):
        return sum(1 for character in self.text.lower() if character in "aeiou")

    def is_palindrome(self):
        return self.text == self.text[::-1]

operations = StringOperations("madam")
print("Reverse:", operations.reverse())
print("Vowels:", operations.count_vowels())
print("Palindrome:", operations.is_palindrome())
