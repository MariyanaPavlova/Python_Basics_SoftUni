import sys
import math
n = int(input())

even_sum =0
even_max =-sys.maxsize
even_min =sys.maxsize
odd_sum =0
odd_max =-sys.maxsize
odd_min =sys.maxsize

for i in range (1,n+1):
    curr_num = float(input())
    if i %2 ==0:
        even_sum +=curr_num
        if curr_num >= even_max:
            even_max = curr_num
        if curr_num <= even_min:
            even_min = curr_num
    elif i%2 !=0:
        odd_sum +=curr_num
        if curr_num >= odd_max:
            odd_max = curr_num
        if curr_num <= odd_min:
            odd_min = curr_num

if odd_sum%1==0:
    print(f'OddSum={math.floor(odd_sum)},')
else:
    print(f'OddSum={odd_sum},')
if odd_min !=sys.maxsize and odd_min%1 !=0:
    print(f'OddMin={odd_min},')
elif odd_min !=sys.maxsize and odd_min%1 ==0:
    print(f'OddMin={math.floor(odd_min)},')
else:
    print(f'OddMin=No,')
if odd_max !=-sys.maxsize and odd_max%1 !=0:
    print(f'OddMax={odd_max},')
elif odd_max !=-sys.maxsize and odd_max%1 ==0:
    print(f'OddMax={math.floor(odd_max)},')
else:
    print(f'OddMax=No,')

if even_sum%1==0:
    print(f'EvenSum={math.floor(even_sum)},')
else:
    print(f'EvenSum={even_sum},')
if even_min !=sys.maxsize and even_min%1 !=0:
    print(f'EvenMin={even_min},')
elif even_min !=sys.maxsize and even_min%1 ==0:
    print(f'EvenMin={math.floor(even_min)},')
else:
    print(f'EvenMin=No,')
if even_max !=-sys.maxsize and even_max%1 !=0:
    print(f'EvenMax={even_max}')
elif even_max !=-sys.maxsize and even_max%1 ==0:
    print(f'EvenMax={math.floor(even_max)},')
else:
    print(f'EvenMax=No')
