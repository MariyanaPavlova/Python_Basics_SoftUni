bevarage = input()
sugar = input()
count = int(input())
price =0

if bevarage == 'Espresso':
    if sugar == 'Without':
        price = (count *0.90)
        price = price-price * 0.35
    else:
        price = count * 0.90
    if sugar == 'Normal':
        price = count * 1.00
    elif sugar == 'Extra':
        price = count * 1.20
    if count >=5:
        price = price - price*0.25

elif bevarage == 'Cappuccino':
    if sugar == 'Without':
        price = count * 1.00
        price = price - price * 0.35
    else:
        price = count * 0.90
    if sugar == 'Normal':
        price = count * 1.20
    elif sugar == 'Extra':
        price = count * 1.60

elif bevarage == 'Tea':
    if sugar == 'Without':
        price = (count *0.50)
        price = price-price * 0.35
    else:
        price = count * 0.90
    if sugar == 'Normal':
        price = count * 0.6
    elif sugar == 'Extra':
        price = count * 0.70
if price > 15:
    price = price - price *0.20

print(f'You bought {count} cups of {bevarage} for {price:.2f} lv.')