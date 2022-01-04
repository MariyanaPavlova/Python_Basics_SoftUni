name = input()

fin_win=0
fin_lose=0
fin_match=0

while name != 'End of tournaments':
    match = int(input())
    fin_match+=match
    for i in range(1, match+1):
        point1=int(input())
        point2=int(input())
        if point1 > point2:
            win=point1-point2
            fin_win +=1
            print(f'Game {i} of tournament {name}: win with {win} points.')
        else:
            lose = point2-point1
            fin_lose +=1
            print(f'Game {i} of tournament {name}: lost with {lose} points.')
    name = input()
aver_win=fin_win/fin_match*100
aver_lose=fin_lose/fin_match*100

print(f'{aver_win:.2f}% matches win')
print(f'{aver_lose:.2f}% matches lost')