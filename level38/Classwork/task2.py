def manual_max(arr):
    max_number = arr[0]
    for num in arr:
        if num > max_number:
            max_number = num
    return max_number


def manual_len(arr):
    count = 0
    for len in arr:
        count += 1
    return count
