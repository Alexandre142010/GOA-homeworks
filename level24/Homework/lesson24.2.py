list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
count = 0
for i in list[::-1] :
    if count % 2 == 0:
        print(i)

    count += 1