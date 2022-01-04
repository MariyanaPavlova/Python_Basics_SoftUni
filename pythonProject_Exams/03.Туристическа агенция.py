town = input()
package = input()
discount = input()
days = int(input())
price =0

if days < 1 and (town == 'Bansko' or town == 'Borovets'or town =='Varna' or town == 'Burgas'):
    print('Days must be positive number!')
elif days > 7:
    days = days-1
else:
    days = days

if town == 'Bansko' or town == 'Borovets':
    if package == 'withEquipment':
        price = 100
        if discount == 'yes':
            price = price - price * 0.10
        else:
            price = price
    elif package == 'noEquipment':
        price = 80
        if discount == 'yes':
            price = price - price * 0.05
        else:
            price = price
    else:
        print("Invalid input!")
    sum = days * price
    if sum >0:
        print(f"The price is {sum:.2f}lv! Have a nice time!")
elif town == 'Varna' or town == 'Burgas':
    if package == 'withBreakfast':
        price = 130
        if discount == 'yes':
            price = price - price * 0.12
        else:
            price = price
    elif package == 'noBreakfast':
        price = 100
        if discount == 'yes':
            price = price - price * 0.07
        else:
            price = price
    else:
        print("Invalid input!")
    sum = days * price
    if sum >0:
        print(f"The price is {sum:.2f}lv! Have a nice time!")
else:
    print("Invalid input!")
