name = input()
count = int(input())

countW = 0
countD = 0
countL = 0
points = 0

for i in range(count):
    result = input()
    if result == 'W':
        countW +=1
        points +=3
    elif result == 'D':
        countD +=1
        points +=1
    elif result == 'L':
        countL +=1
        points +=0

if count ==0:
    print(f"{name} hasn't played any games during this season")
else:
    perc = countW / count*100
    print(f'{name} has won {points} points during this season.')
    print("Total stats:")
    print(f'## W: {countW}')
    print(f'## D: {countD}')
    print(f'## L: {countL}')
    print(f"Win rate: {perc:.2f}%")