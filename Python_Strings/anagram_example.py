word1 = input("enter the first word: ")
word2 = input("enter the second word: ")
if sorted(word1) == sorted(word2):
    print("Anagram")
else:
    print("Not A Anagram")