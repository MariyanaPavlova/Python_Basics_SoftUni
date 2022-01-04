budget = float(input())
count_ser = int(input())
summ = 0

for i in range(count_ser):
    name = input()
    price = float(input())

    if name == 'Thrones':
        summ += price - price *0.50
    elif name == 'Lucifer':
        summ += price - price *0.40
    elif name == 'Protector':
        summ += price - price *0.30
    elif name == 'TotalDrama':
        summ += price - price *0.20
    elif name == 'Area':
        summ += price - price *0.10
    else:
        summ += price
    diff = abs(budget-summ)
if budget >= summ:
    print(f'You bought all the series and left with {diff:.2f} lv.')

else:
    print(f'You need {diff:.2f} lv. more to buy the series!')