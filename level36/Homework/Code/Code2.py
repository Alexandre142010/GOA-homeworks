#https://www.codewars.com/kata/5769b3802ae6f8e4890009d2/train/python
#Removing Elements
def remove_every_other(arr):
    
    result = []
    
    
    for i in range(len(arr)):
        if i % 2 == 0:  
            result.append(arr[i])
    
    return result