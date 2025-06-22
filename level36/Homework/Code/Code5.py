#https://www.codewars.com/kata/567bf4f7ee34510f69000032/train/python
#Regexp Basics - is it a digit?
def digit(n):
    return isinstance(n, str) and len(n) == 1 and n.isdigit()