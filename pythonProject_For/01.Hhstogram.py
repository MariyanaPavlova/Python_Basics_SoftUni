n = int(input())

p1 = 0
p2 = 0
p3 = 0
p4 = 0
p5 = 0

for i in range(n):
    number = int(input())
    if number < 200:
        p1 += 1
    elif 200 <= number <= 399:
        p2 += 1
    elif number <= 599:
        p3 += 1
    elif number <= 799:
        p4 += 1
    else:
        p5 += 1
persent1 = p1 / n * 100
persent2 = p2 / n * 100
persent3 = p3 / n * 100
persent4 = p4 / n * 100
persent5 = p5 / n * 100
print(f'{persent1:.2f}%')
print(f'{persent2:.2f}%')
print(f'{persent3:.2f}%')
print(f'{persent4:.2f}%')
print(f'{persent5:.2f}%')
