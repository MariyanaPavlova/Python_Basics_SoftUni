fruit = input()
sett = input()
count = int(input())

if sett == 'small':
    if fruit == 'Watermelon':
        price = 56 * 2
    elif fruit == 'Mango':
        price = 36.66 * 2
    elif fruit == 'Pineapple':
        price = 42.10 * 2
    elif fruit == 'Raspberry':
        price = 20 * 2
elif sett == 'big':
    if fruit == 'Watermelon':
        price = 28.70 * 5
    elif fruit == 'Mango':
        price = 19.60 * 5
    elif fruit == 'Pineapple':
        price = 24.80 * 5
    elif fruit == 'Raspberry':
        price = 15.20 * 5
price_fin = price * count
if 400 <= price_fin <= 1000:
    discount = price_fin - price_fin * 0.15
elif price_fin > 1000:
    discount = price_fin - price_fin * 0.50
else:
    discount = price_fin

print(f'{discount:.2f} lv.')
