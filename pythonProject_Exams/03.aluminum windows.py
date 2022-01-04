count = int(input())
tiipe = input()
delivery = input()
price =0
if count < 10:
    print('Invalid order')
else:
    if tiipe == '90X130':
        if 30 <= count <= 60:
            price = count*(110-110*0.05)
        elif count >60:
            price = count*(110 - 110*0.08)
        else:
            price = count*110
    elif tiipe == '100X150':
        if 40 <= count <= 80:
            price = count*(140 - 140 * 0.06)
        elif count > 80:
            price = count*(140 - 140 * 0.10)
        else:
            price = count*140
    elif tiipe == '130X180':
        if 20 <= count <= 50:
            price = count*(190 - 190 * 0.07)
        elif count > 50:
            price = count*(190 - 190 * 0.12)
        else:
            price = 190*count
    elif tiipe == '200X300':
        if 25 <= count <= 50:
            price = count*(250 - 250 * 0.09)
        elif count > 50:
            price = count*(250 - 250 * 0.14)
        else:
            price = 250*count

    if delivery == 'With delivery':
        price = price + 60
    else:
        price = price
    if count > 99:
        price = price-price*0.04

    if price != 0:
        print(f'{price:.2f} BGN')
#    else:
 #       print('Invalid order')