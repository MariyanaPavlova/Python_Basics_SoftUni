type = input().lower()
r = int(input())
c = int(input())

full = r * c
income = 0

if type == 'premiere':
    income = full * 12
elif type == 'normal':
    income = full * 7.50
elif type == 'discount':
    income = full * 5.00
print(f'{income:.2f} leva')
