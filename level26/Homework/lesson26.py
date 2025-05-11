Starter_number = input("Starter number:")
Finisher_number = input("Finisher number:")
if Finisher_number < Starter_number:
    print("Araswori shualedi")
for i in range(int(Starter_number), int(Finisher_number) + 1):
    print(i)

sum = 0
for i in range(int(Starter_number), int(Finisher_number) + 1):
    sum += i
print("Sum of numbers:", sum)