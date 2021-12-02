budget=float(input())
count_stat=int(input())
prize_cloths_stat=float(input())

decor=budget*0.1
prize_clothes=count_stat*prize_cloths_stat
if count_stat > 150:
    discount=prize_clothes*0.1
else:
    discount=0
disc = prize_clothes-discount
sum=decor+disc

money_remain=abs(budget-sum)
if sum <= budget:
    print('Action!')
    print(f'Wingard starts filming with {money_remain:.2f} leva left.')
else:
    print('Not enough money!')
    print(f'Wingard needs {money_remain:.2f} leva more.')


