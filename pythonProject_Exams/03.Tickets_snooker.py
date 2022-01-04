etap = input()
tipe = input()
count=int(input())
photo = input()

price=0
price_Y=0
if etap == 'Quarter final':
    if tipe == 'Standard':
        price = 55.50*count
    elif tipe == 'Premium':
        price = 105.20*count
    elif tipe == 'VIP':
        price = 118.90*count
elif etap == 'Semi final':
    if tipe == 'Standard':
        price = 75.88*count
    elif tipe == 'Premium':
        price = 125.22*count
    elif tipe == 'VIP':
        price = 300.40*count
elif etap == 'Final':
    if tipe == 'Standard':
        price = 110.10*count
    elif tipe == 'Premium':
        price = 160.66*count
    elif tipe == 'VIP':
        price = 400*count

if 2500 < price <= 4000:
    price = price-price*0.10
elif price > 4000:
    price = price - price*0.25
    price_Y=price

if photo == "Y":
    if price_Y !=0:
        price = price
    else:
        price=price+count*40
else:
    price=price
print(f'{price:.2f}')

