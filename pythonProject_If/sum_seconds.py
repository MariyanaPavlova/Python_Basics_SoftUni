a = int(input())
b = int(input())
c = int(input())

sum = a + b + c
sum_min = sum // 60
sum_sec = sum % 60

if sum_sec < 10:
    print(f'{sum_min}:0{sum_sec}')
else:
    print(f'{sum_min}:{sum_sec}')
