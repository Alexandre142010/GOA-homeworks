set = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
def set_operations(input_set):
    input_set.add(11)
    input_set.add(492)
    input_set.add(1000)
    input_set.remove(1)
    return input_set
print(set_operations(set))