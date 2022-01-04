guests = int(input())
kuvert = float(input())
budget = float(input())
price=0

if 10 <= guests <= 15:
    price = kuvert-kuvert*0.15
elif 15 < guests <= 20:
    price = kuvert-kuvert*0.20
elif guests >20:
    price = kuvert-kuvert*0.25
else:
    price = kuvert
cake = budget*0.10
total = cake+price*guests
diff = abs(budget-total)
if budget >= total:
    print(f'It is party time! {diff:.2f} leva left.')
else:
    print(f'No party! {diff:.2f} leva needed.')