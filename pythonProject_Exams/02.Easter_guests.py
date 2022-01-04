import math

guests = int(input())
budget = int(input())

kozun = math.ceil(guests/3)
eggs = guests*2

price_kozun = kozun*4
price_eggs = eggs * 0.45
total = price_eggs+price_kozun
diff=abs(budget-total)
if total <= budget:
    print(f'Lyubo bought {kozun} Easter bread and {eggs} eggs.')
    print(f'He has {diff:.2f} lv. left.')
else:
    print(f"Lyubo doesn't have enough money.")
    print(f'He needs {diff:.2f} lv. more.')
