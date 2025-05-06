Random_word = input("Enter a random word: ")
if Random_word == Random_word[::-1]:
    print("The word is a palindrome")
else:
    print("The word is a normal word")