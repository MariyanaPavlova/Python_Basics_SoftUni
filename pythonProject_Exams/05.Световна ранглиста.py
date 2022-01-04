import math

count = int(input())
point = int(input())

points = point
countW=0
points_tur=0

for i in range(count):
    position = input()

    if position == 'W':
        points += 2000
        points_tur +=2000
        countW +=1
    elif position == "F":
        points += 1200
        points_tur += 1200
    elif position == 'SF':
        points += 720
        points_tur += 720

aver = math.floor(points_tur/count)
perc = countW/count*100

print(f'Final points: {points}')
print(f'Average points: {aver}')
print(f'{perc:.2f}%')

