import sys
n = int(input())
max = - sys.maxsize
sum = 0

for i in range(n):
    curr_num = int(input())
    sum += curr_num

    if curr_num >= max:
        max = curr_num
sum -= max

if max == sum:
    print('Yes')
    print(f'Sum = {max}')
else:
    diff = abs(sum - max)
    print('No')
    print(f'Diff = {diff}')
