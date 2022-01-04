kg = float(input())
tipe = input()
km = int(input())
price = 0
price_n =0

if kg < 1.00:
    price = 0.03 * km
    if tipe == 'express':
        price_n =(0.03*0.80)*kg*km

elif 1<= kg < 10:
    price = 0.05 * km
    if tipe == 'express':
        price_n =(0.05*0.40)*kg*km

elif 10<= kg < 40:
    price = 0.10 * km
    if tipe == 'express':
        price_n = (0.10*0.05)*kg*km
elif 40<= kg < 90:
    price = 0.15 * km
    if tipe == 'express':
        price_n = (0.15*0.02)*kg*km

elif 90<= kg < 150:
    price = 0.20 * km
    if tipe == 'express':
        price_n = (0.20*0.01)*kg*km

total = price+price_n
print(f'The delivery of your shipment with weight of {kg:.3f} kg. would cost {total:.2f} lv.')
