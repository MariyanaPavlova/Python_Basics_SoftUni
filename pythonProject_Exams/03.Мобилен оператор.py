contract = input()
tipe_contract = input()
internet = input()
month = int(input())
price = 0

if contract == 'one':
    if tipe_contract == 'Small':
        price = 9.98
    elif tipe_contract == 'Middle':
        price = 18.99
    elif tipe_contract == 'Large':
        price = 25.98
    elif tipe_contract == 'ExtraLarge':
         price = 35.99
elif contract == 'two':
    if tipe_contract == 'Small':
        price = 8.58
    elif tipe_contract == 'Middle':
        price = 17.09
    elif tipe_contract == 'Large':
        price = 23.59
    elif tipe_contract == 'ExtraLarge':
        price = 31.79
if internet == "yes":
    if price <= 10:
        price +=5.50
    elif 10<price <=30:
        price +=4.35
    elif price >30:
        price +=3.85
if contract == 'two':
    discount = price*3.75/100
else:
    discount =0
total = price - discount
total_amount = total*month
print(f'{total_amount:.2f} lv.')
