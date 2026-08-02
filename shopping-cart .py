foods = []
price = []
total = 0

while True:
    food = input("enter the food time (or 'done' to finish): " )
    if food.lower() == "done":
        break
    else:
        p=float(input(f"enter the price of the {food}:  "))
        foods.append(food)
        price.append(p)

print("----your shopping cart----")

for food in foods:
    print(food, end = " ")

for p in price:
    total +=p

print(f"\nTotal price: {total}")




