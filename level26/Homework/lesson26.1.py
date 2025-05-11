Fruits = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape", "honeydew"]
input_fruit = input("Enter your favourite fruit: ")
if input_fruit in Fruits:
    print("Your favourite fruit is in the list.")
fruit_in_basket = False
for fruit in Fruits:
    if fruit == input_fruit:
        fruit_in_basket = True
if fruit_in_basket:
    print("Good choice")
else:
    print("Fruit not in basket")