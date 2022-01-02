destination = input()

while destination != "End":
    needed_money = float(input())
    saved_money = 0
    #if destination == 'End':
        #break
    while saved_money < needed_money:
        money = float(input())
        saved_money += money
    print(f'Going to {destination}!')

    destination = input()
