count = int(input())

red = 0
orange =0
blue =0
green = 0
max =0
coloree=None

for i in range(count):
    color = input()

    if color == 'red':
        red += 1
        if red >max:
            max=red
            coloree=color
    elif color == 'orange':
        orange +=1
        if orange >max:
            max=orange
            coloree=color
    elif color == 'blue':
        blue +=1
        if blue > max:
            max = blue
            coloree=color
    elif color == 'green':
        green +=1
        if green > max:
            max = green
            coloree=color

print(f'Red eggs: {red}')
print(f'Orange eggs: {orange}')
print(f'Blue eggs: {blue}')
print(f'Green eggs: {green}')
print(f'Max eggs: {max} -> {coloree}')