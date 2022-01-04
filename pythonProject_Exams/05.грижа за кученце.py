food = int(input())
gr = food * 1000
daily_eaten = 0

while True:
    eaten_food = input()
    if eaten_food == 'Adopted':
        break
    eaten_food_i = int(eaten_food)
    daily_eaten += eaten_food_i
diff = abs(gr-daily_eaten)
if daily_eaten <= gr:
    print(f"Food is enough! Leftovers: {diff} grams.")
else:
    print(f"Food is not enough. You need {diff} grams more.")
