luguage_price = float(input())
luguage_kg = float(input())
days_trip = int(input())
luguage_count = int(input())
taksa = 0

if luguage_kg < 10:
    taksa =  luguage_price * 0.20
elif 10 <= luguage_kg <= 20:
    taksa = luguage_price * 0.50
elif luguage_kg >20:
    taksa=luguage_price
if days_trip > 30:
    taksa = taksa + taksa * 0.10
elif 7 <= days_trip <= 30:
    taksa = taksa + taksa * 0.15
elif days_trip < 7:
    taksa = taksa + taksa * 0.40

sum = luguage_count * taksa
print(f'The total price of bags is: {sum:.2f} lv.')
