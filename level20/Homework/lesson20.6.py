sentence = input("Enter a sentence: ")
vowels_count = 0
consonant_count = 0
lenght = 0
for char in sentence:
    if char == "a" or char == "A":
        vowels_count += 1
    elif char == "e" or char == "E":
        vowels_count += 1
    elif char == "i" or char == "I":
        vowels_count += 1
    elif char == "o" or char == "O":
        vowels_count += 1
    elif char == "u" or char == "U":
        vowels_count += 1
    else:
        consonant_count += 1
    lenght += 1
print("Number of consonants in the sentence:", consonant_count)
print("Number of vowels in the sentence:", vowels_count)
print("Length of the sentence:", lenght)

