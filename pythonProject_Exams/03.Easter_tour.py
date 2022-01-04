destination = input()
date = input()
nigths = int(input())

if date == '21-23':
    if destination == 'France':
        price = nigths * 30
    elif destination == 'Italy':
        price = nigths * 28
    elif destination == 'Germany':
        price = nigths * 32
elif date == '24-27':
    if destination == 'France':
        price = nigths * 35
    elif destination == 'Italy':
        price = nigths * 32
    elif destination == 'Germany':
        price = nigths * 37
elif date == '28-31':
    if destination == 'France':
        price = nigths * 40
    elif destination == 'Italy':
        price = nigths * 39
    elif destination == 'Germany':
        price = nigths * 43

print(f'Easter trip to {destination} : {price:.2f} leva.')