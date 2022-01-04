budget = float(input())
fuel = float(input())
day = input()

fuel_price = fuel*2.10
gide = 100
total = fuel_price+gide
if day == 'Sunday':
    total = total-total*0.20
elif day == 'Saturday':
    total = total-total*0.10

diff = abs(budget-total)
if budget >= total:
    print(f'Safari time! Money left: {diff:.2f} lv.')
else:
    print(f'Not enough money! Money needed: {diff:.2f} lv.')
