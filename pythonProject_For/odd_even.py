n = int(input())
even_sum = 0
odd_sum = 0

for i in range(n):
    num = int(input())
    if i % 2 == 0:
        even_sum += num
    else:
        odd_sum += num

if even_sum == odd_sum:
    print('Yes')
    print('Sum = ' + str(even_sum))
else:
    diff = abs(even_sum - odd_sum)
    print('No')
    print('Diff = ' + str(diff))
