a=float(input())
b=float(input())

s=a*b
count=0
remain=0

while remain >= 0:
    piece = input()
    if piece != 'STOP':
        count += int(piece)
        remain = s - count

    if piece == 'STOP':
        print(f'{remain:.0f} pieces are left.')
        break
    elif remain <= 0:
        print(f"No more cake left! You need {abs(remain):.0f} pieces more.")
