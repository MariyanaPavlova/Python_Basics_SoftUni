budget = int(input())
season = input()
count_fishman = int(input())

price = 0

if season == 'Spring':
    price = 3000
elif season == 'Autumn' or season == 'Summer':
    price = 4200
elif season == 'Winter':
    price = 2600

if count_fishman <= 6:
    price = price - price * 0.10
elif count_fishman > 6 and count_fishman <= 11:
    price = price - price * 0.15
else:
    price = price - price * 0.25

if count_fishman % 2 == 0 and season != 'Autumn':
    price = price - price * 0.05

remaining = budget - price
remaining_ = abs(remaining)

if budget >= price:
    print (f"Yes! You have {remaining_:.2f} leva left.")
else:
    print(f"Not enough money! You need {remaining_:.2f} leva.")