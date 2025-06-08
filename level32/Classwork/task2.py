def square_properties(length = 10):
    area = length ** 2
    perimeter = 4 * length
    return area, perimeter
square_area1, square_perimeter1 = square_properties(5)
square_area2, square_perimeter2 = square_properties()
print(square_area1, square_perimeter1)
print(square_area2, square_perimeter2)