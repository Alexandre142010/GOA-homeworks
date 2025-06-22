#https://www.codewars.com/kata/57a5b0dfcf1fa526bb000118/train/python
#Remove duplicates from list
def distinct(seq):
    seen = set()
    return [x for x in seq if not (x in seen or seen.add(x))]