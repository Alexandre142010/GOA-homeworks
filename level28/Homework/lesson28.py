#Upper() tasks
#1) 
word = input("Enter a word: ")
print(word.upper())
#2)
word1 = input("Enter a word: ")
print(word1.upper())
word2 = input("Enter a word: ")
print(word2.lower())
print(word1 == word2)
#3)
list = ["Georgia," "Armenia", "Greece", "Norway", "Denmark"]
for i in list:
    print(i.lower())
#Upper() tasks
#1)
word = input("Enter a word: ")
print(word.upper())
#2)
list = ["Georgia", "Armenia", "Greece", "Norway", "Denmark"]
for i in list:
    print(i.upper())
#3)
word = input("Enter a word: ")
if word == word.upper():
    print("The word is in uppercase.")
else:
    print("The word is not in uppercase.")
#Capitalize() tasks
#1)
word = input("Enter a word: ")
print(word.capitalize())
#2)
word = "gEoRGia"
print(word.capitalize())
#3)
list = ["georgia", "aRMENIA", "greeCE"]
for i in list:
    print(i.lower().capitalize())
#find() tasks
#1)
word = input("Enter a word: ")
print(word.find("a"))
#2)
word = "I visited Georgia, Armenia and Greece"
print(word.find("Armenia"))
#3)
word = "Hello"
word_to_find = input("Enter a word to find: ")
if word.find(word_to_find):
    print(f"Word found at position: {word.find(word_to_find)}")
else:
    print("Word not found")