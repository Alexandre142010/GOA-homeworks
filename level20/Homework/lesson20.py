choose_number = int(input("Choose a random number: "))

if choose_number < 0 and choose_number % 2 != 0:
    print("The number is negative and odd")
if choose_number > 0 and choose_number % 2 == 0:
    print("The number is positive and even")
if choose_number == 0:
    print("The number is zero")