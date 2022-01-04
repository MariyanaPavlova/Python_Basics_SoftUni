name1=input()
name2=input()

points1=0
points2=0
points11 = 0
points22 = 0
name11=None
name22=None

while True:
    card1 = input()

    if card1 == 'End of game':
        print(f'{name1} has {points1} points')
        print(f'{name2} has {points2} points')
        exit()
    card1 = int(card1)
    card2 = int(input())
    if card1 > card2:
        points1 +=card1-card2
    elif card2 > card1:
        points2 +=card2-card1
    elif card1 == card2:
        print(f'Number wars!')
        card11 =int(input())
        card22 =int(input())
        if card11 > card22:
            points11 = card11-card22
            name11=name1
        else:
            points22 = card22-card11
            name22=name2
        if points11 > points22:
            print(f'{name11} is winner with {points1} points')
        else:
            print(f'{name22} is winner with {points2} points')
        exit()

