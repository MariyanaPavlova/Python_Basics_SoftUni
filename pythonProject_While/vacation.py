needed_money = float(input())
owned_money = float(input())
day_count = 0
day_spend = 0

while owned_money < needed_money and day_spend < 5:
    actionn = input()
    amount = float(input())
    day_count += 1
    if actionn == 'save':
        owned_money += amount
        day_spend = 0
    elif actionn == 'spend':
        owned_money -= amount
        day_spend += 1
        if owned_money < 0:
            owned_money = 0
        if day_spend == 5:
            print("You can't save the money.")
            print(f'{day_count}')
            break
if owned_money >= needed_money:
    print(f'You saved the money for {day_count} days.')

