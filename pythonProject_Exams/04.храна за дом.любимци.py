days = int(input())
food = float(input())
food_dog_total = 0
food_cat_total = 0
total_food = 0
biscuits_tot = 0

for i in range(1, days + 1):
    dog = int(input())
    cat = int(input())
    food_day = dog + cat
    food_dog_total += dog
    food_cat_total += cat

    if i % 3 == 0:
        biscuits = food_day * 0.10
        biscuits_tot += biscuits

total_food = food_dog_total + food_cat_total
pers_dog = food_dog_total / total_food * 100
pers_cat = food_cat_total / total_food * 100
pers_total = total_food / food * 100

print(f"Total eaten biscuits: {round(biscuits_tot)}gr.")
print(f"{pers_total:.2f}% of the food has been eaten.")
print(f"{pers_dog:.2f}% eaten from the dog.")
print(f"{pers_cat:.2f}% eaten from the cat.")
