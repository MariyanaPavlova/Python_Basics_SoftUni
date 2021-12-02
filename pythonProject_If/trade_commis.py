town = input().lower()
sales = float(input())
pers = 0

if town == 'sofia':
    if 0 <= sales <= 500:
        pers = sales * 0.05
    elif 500 <= sales <= 1000:
        pers = sales * 0.07
    elif 1000 <= sales <= 10000:
        pers = sales * 0.08
    elif sales > 10000:
        pers = sales * 0.12
if town == 'varna':
    if 0 <= sales <= 500:
        pers = sales * 4.5 / 100
    elif 500 <= sales <= 1000:
        pers = sales * 7.5 / 100
    elif 1000 <= sales <= 10000:
        pers = sales * 10 / 100
    elif sales > 10000:
        pers = sales * 13 / 100
if town == 'plovdiv':
    if 0 <= sales <= 500:
        pers = sales * 5.5 / 100
    elif 500 <= sales <= 1000:
        pers = sales * 8 / 100
    elif 1000 <= sales <= 10000:
        pers = sales * 12 / 100
    elif sales > 10000:
        pers = sales * 14.5 / 100
if pers > 0:
    print(f'{pers:.2f}')
else:
    print('error')
