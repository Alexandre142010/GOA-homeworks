#https://www.codewars.com/kata/54ba84be607a92aa900000f1/train/python
#Isograms
def is_isogram(string):
    string = string.lower()
    seen = set()
    for char in string:
        if char in seen:
            return False
        seen.add(char)
    return True