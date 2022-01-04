film = input()
packet = input()
count = int(input())

if film == 'John Wick':
    if packet == 'Drink':
        price = count*12
    elif packet == 'Popcorn':
        price = count*15
    elif packet == 'Menu':
        price = count*19

elif film == 'Star Wars':
    if packet == 'Drink':
        price = count * 18
    elif packet == 'Popcorn':
        price = count * 25
    elif packet == 'Menu':
        price = count * 30
    if count >=4:
        price = price - price*0.30

elif film == 'Jumanji':
    if packet == 'Drink':
        price = count * 9
    elif packet == 'Popcorn':
        price = count * 11
    elif packet == 'Menu':
        price = count * 14
    if count == 2:
        price = price - price * 0.15

print(f'Your bill is {price:.2f} leva.')