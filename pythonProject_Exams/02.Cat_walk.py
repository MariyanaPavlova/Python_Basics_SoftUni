min_walk = int(input())
count_walk = int(input())
calories = int(input())

walk = min_walk * count_walk
burned_cal = walk * 5
pers = calories * 0.50
if burned_cal >= pers:
    print(f"Yes, the walk for your cat is enough. Burned calories per day: {burned_cal}.")
else:
    print(f"No, the walk for your cat is not enough. Burned calories per day: {burned_cal}.")
