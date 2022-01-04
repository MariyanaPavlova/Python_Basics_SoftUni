budget = float(input())
destination = input()
season = input()
days = int(input())
price =0
if destination == 'Dubai':
    if season == "Winter":
        price = 45000 * days
        price -= price * 0.30
    elif season == 'Summer':
        price = 40000 * days
        price -= price * 0.30
elif destination == 'Sofia':
    if season == "Winter":
        price = 17000 * days
        price += price * 0.25
    elif season == 'Summer':
        price = 12500 * days
        price += price * 0.25
elif destination == 'London':
    if season == "Winter":
        price = 24000 * days
    elif season == 'Summer':
        price = 20250 * days
diff = abs(budget - price)
if budget >= price:
    print(f"The budget for the movie is enough! We have {diff:.2f} leva left!")
else:
    print(f'The director needs {diff:.2f} leva more!')