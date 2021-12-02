budget=float(input())
category=input().lower()
people=int(input())

rem_budget=None
money_for_ticket=None

if category == "vip":
    money_for_ticket = 499.99 * people
elif category == 'normal':
    money_for_ticket = 249.99 * people

if people <= 4:
    rem_budget = budget - budget * 0.75
elif people <=9:
    rem_budget  = budget - budget * 0.60
elif people <= 24:
    rem_budget  = budget - budget * 0.50
elif people <= 49:
    rem_budget  = budget - budget * 0.40
else:
    rem_budget  = budget - budget * 0.25

diff = rem_budget - money_for_ticket
diff_abs=abs(diff)

if diff >0:
    print(f'Yes! You have {diff_abs:.2f} leva left.')
else:
    print(f'Not enough money! You need {diff_abs:.2f} leva.')
