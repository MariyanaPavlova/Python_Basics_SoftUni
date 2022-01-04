name = input()

points = 301
count =0
count_n=0

while points > 0:
    field = input()

    if field == 'Retire':
        print(f'{name} retired after {count_n} unsuccessful shots.')
        exit()
    point = int(input())

    if field == 'Single':
        if point <= points:
            points -= point
            count +=1
        else:
            count_n +=1
    elif field == 'Double':
        if point*2 <= points:
            points -= point*2
            count +=1
        else:
            count_n += 1
    elif field == 'Triple':
        if point*3 <= points:
            points -= point*3
            count +=1
        else:
            count_n += 1
print(f'{name} won the leg with {count} shots.')
