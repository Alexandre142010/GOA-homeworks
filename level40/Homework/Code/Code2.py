#https://www.codewars.com/kata/55a2d7ebe362935a210000b2/train/python
#Find the smallest integer in the array
def find_smallest_int(arr):
    if not arr:  
        return None
    smallest = arr[0]  
    for num in arr:
        if num < smallest:  
            smallest = num
    return smallest  