name = input()
days = int(input())
tickets = int(input())
price = float(input())
perc = int(input())

price = tickets*price
tot_price = price*days
perc = tot_price*perc/100
profit = tot_price - perc

print(f'The profit from the movie {name} is {profit:.2f} lv.')