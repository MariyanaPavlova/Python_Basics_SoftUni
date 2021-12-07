age = int(input())
washing_mashine = float(input())
toy_price = float(input())

money = 0
savings = 0
toy_count = 0

for year in range(1, age + 1):
    if year % 2 == 0:
        money += 10
        savings += money - 1
    else:
        toy_count += 1
toy_money = toy_price * toy_count
total = savings + toy_money
diff = abs(total - washing_mashine)

if total >= washing_mashine:
    print(f'Yes! {diff:.2f}')
else:
    print(f'No! {diff:.2f}')
