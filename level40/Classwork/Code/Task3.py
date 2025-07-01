#https://www.codewars.com/kata/57a1fd2ce298a731b20006a4/train/python
#Is it a palindrome?
def is_palindrome(s):
    normalized_string = s.lower()
    return normalized_string == normalized_string[::-1]