#https://www.codewars.com/kata/57cebe1dc6fdc20c57000ac9/train/python
#Shortest Word

def find_short(s):
    words = s.split()
    shortest_length = min(len(word) for word in words)
    return shortest_length