import math
ball = int(input())
points_total=0
red=0
orange=0
yellow=0
white=0
other_color=0
black=0

for i in range(ball):
    color = input()
    if color == 'red':
        points_total +=5
        red +=1
    elif color == 'orange':
        points_total +=10
        orange+=1
    elif color == 'yellow':
        points_total +=15
        yellow +=1
    elif color == 'white':
        points_total +=20
        white +=1
    elif color == 'black':
        points_total = math.floor(points_total/2)
        black+=1
    else:
        points_total+=0
        other_color +=1
print(f'Total points: {points_total}')
print(f'Points from red balls: {red}')
print(f'Points from orange balls: {orange}')
print(f'Points from yellow balls: {yellow}')
print(f'Points from white balls: {white}')
print(f'Other colors picked: {other_color}')
print(f'Divides from black balls: {black}')
