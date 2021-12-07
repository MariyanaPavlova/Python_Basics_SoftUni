import sys
n = int(input())
even_sum = 0
even_max = -sys.maxsize
even_min = sys.maxsize
odd_sum = 0
odd_max = -sys.maxsize
odd_min = sys.maxsize

for i in range(1, n + 1):
    curr_num = float(input())
    if i % 2 == 0:
        even_sum += curr_num
        if curr_num >= even_max:
            even_max = curr_num
        if curr_num <= even_min:
            even_min = curr_num
    elif i % 2 != 0:
        odd_sum += curr_num
        if curr_num >= odd_max:
            odd_max = curr_num
        if curr_num <= odd_min:
            odd_min = curr_num

print(f'OddSum={odd_sum:.2f},')
if odd_max != -sys.maxsize:
    print(f'OddMin={odd_min:.2f},')
else:
    print(f'OddMin=No,')
if odd_min != sys.maxsize:
    print(f'OddMax={odd_max:.2f},')
else:
    print(f'OddMax=No,')
print(f'EvenSum={even_sum:.2f},')
if even_max != -sys.maxsize:
    print(f'EvenMin={even_min:.2f},')
else:
    print(f'EvenMin=No,')
if even_min != sys.maxsize:
    print(f'EvenMax={even_max:.2f}')
else:
    print(f'EvenMax=No')
