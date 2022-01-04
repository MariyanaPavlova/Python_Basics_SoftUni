chicken = int(input())
fish = int(input())
vegan = int(input())

all_price = chicken * 10.35 + fish * 12.40 + vegan * 8.15
decert = all_price * 0.20
delivery = 2.50
all = all_price+decert+delivery
print(f'Total: {all:.2f}')