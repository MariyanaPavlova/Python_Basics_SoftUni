n = int(input())

p1 = 0
p2 = 0
p3 = 0


for i in range(n):
    number = int(input())
    if number % 2==0:
        p1 += 1
    if number % 3==0:
        p2 += 1
    if number % 4==0:
        p3 += 1

persent1 = p1 / n * 100
persent2 = p2 / n * 100
persent3 = p3 / n * 100

print(f'{persent1:.2f}%')
print(f'{persent2:.2f}%')
print(f'{persent3:.2f}%')
