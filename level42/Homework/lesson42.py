numbers = {4, 7, 9, 40, 58, 792, 572, 6997}
numbers.add(1000)
numbers.add(88)
numbers.remove(4)
numbers.discard(7)
print(numbers)
even_numbers = {79, 483, 1000, 99, 30, 792, 512}
print(numbers.intersection(even_numbers))
print(numbers.union(even_numbers))
print(numbers.difference(even_numbers))
print(even_numbers.difference(numbers))
print(even_numbers.union(numbers))
print(even_numbers.intersection(numbers))