games = int(input())

hearthstone = 0
fornite =0
overwatch =0
other = 0

for i in range(games):
    name = input()
    if name == 'Hearthstone':
        hearthstone += 1
    elif name == 'Fornite':
        fornite +=1
    elif name == 'Overwatch':
        overwatch +=1
    else:
        other +=1
perc_hearthstone = hearthstone/games *100
perc_fornite = fornite/games *100
perc_overwatch = overwatch/games *100
perc_other = other/games *100
print(f'Hearthstone - {perc_hearthstone:.2f}%')
print(f'Fornite - {perc_fornite:.2f}%')
print(f'Overwatch - {perc_overwatch:.2f}%')
print(f'Others - {perc_other:.2f}%')
