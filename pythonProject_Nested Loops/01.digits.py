n=int(input())

n1 = n // 100
n2 = n//10%10
n3 = n % 10

row_count = int(n1+n2)
count_on_row = int(n1+n3)

for row in range(row_count,0, -1):
    for count in range(count_on_row,0, -1):
        if n % 5 == 0:
            n -= n1
            print(f'{n} ', end='')
        elif n % 3 == 0:
            n -= n2
            print(f'{n} ', end='')
        else:
            n += n3
            print(f'{n} ', end='')

    print()


