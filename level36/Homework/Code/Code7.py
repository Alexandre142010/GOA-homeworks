#https://www.codewars.com/kata/57aa218e72292d98d500240f/train/python
#Heron's formula
def heron(a, b, c):
    s = (a + b + c) / 2
    return (s * (s - a) * (s - b) * (s - c)) ** 0.5 if s > a and s > b and s > c else 0