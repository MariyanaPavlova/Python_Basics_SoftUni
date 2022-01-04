profit = float(input())
coctail = input()
price = 0
summ = 0

while coctail != 'Party!':
    count_coct = int(input())

    name = len(coctail)
    price = count_coct * int(name)

    if price % 2 !=0:
        price = price - price * 0.25
        summ += price
    else:
        price = price
        summ += price
    diff = profit - summ
    if summ >= profit:
        print("Target acquired.")
        print(f"Club income - {summ:.2f} leva.")
        break
    coctail = input()

else:
    print(f'We need {diff:.2f} leva more.')
    print(f"Club income - {summ:.2f} leva.")
