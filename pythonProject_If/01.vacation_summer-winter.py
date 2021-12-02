budget = float(input())
season = input().lower()

price = None
destination = ''
type = None

if season == 'summer':
    type = 'Camp'
    if budget <= 100:
        price = budget * 0.30
        destination = 'Bulgaria'
    elif budget > 100 and budget <= 1000:
        price = budget * 0.40
        destination = 'Balkans'
    elif budget > 1000:
        price = budget * 0.90
        destination = "Europe"

elif season == 'winter':
    type = 'Hotel'
    if budget <= 100:
        price = budget * 0.70
        destination = 'Bulgaria'
    elif budget > 100 and budget <= 1000:
        price = budget * 0.80
        destination = 'Balkans'
    elif budget > 1000:
        price = budget * 0.90
        destination = "Europe"

if destination == 'Europe':
    type = 'Hotel'

print(f'Somewhere in {destination}')
print(f'{type} - {price:.2f}')
