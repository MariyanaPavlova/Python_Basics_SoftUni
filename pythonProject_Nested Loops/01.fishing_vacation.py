limit = int(input())
money_won = 0
money_lost = 0
fishes_count = 0

for i in range (1, limit+1):
    name = input()
    if name == 'Stop':
        break
    fishes_count += 1
    kg = float(input())
    current_price = 0

    for letter in name:     #цикъл за името на рибата -ASCI chr
        current_price += ord(letter)
        current_price /= kg
    if i % 3 == 0:       # за всяка 3 та риба
        money_won += current_price
    else:
        money_lost += current_price

if fishes_count == limit:
    print(f'Lyubo fulfilled the quota!')

money_left = money_won - money_lost
if money_left <0:
    print(f'Lyubo lost {abs(money_left)} leva today')
else:
    print(f'Lyubos profit form {fishes_count} fishes is {money_left} leva')