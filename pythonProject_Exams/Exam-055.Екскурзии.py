sea = int(input())
mount = int(input())

profit = 0

while sea !=0 or mount !=0:
    tipe = input()

    if tipe == 'Stop':
        break
    if tipe == 'sea'and sea >0:
        profit += 680
        if sea >0:
            sea -=1
        else:
            sea -=0
    elif tipe == 'mountain' and mount >0:
        profit += 499
        if mount >0:
            mount -=1
        else:
            mount -=0

if sea ==0 and mount ==0:
    print(f'Good job! Everything is sold.')

print(f'Profit: {profit} leva.')