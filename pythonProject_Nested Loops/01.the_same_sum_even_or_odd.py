num1 = int(input())
num2 = int(input())

for i in range(num1, num2+1):
    even_sum = 0
    odd_sum = 0
    number = i

    for j in range(6):
       curr_num = number % 10
       number //= 10    # маха посл.цифра на number за ясно разбиране
       if j % 2 == 0:
           even_sum += curr_num
       else:
           odd_sum += curr_num
    if odd_sum == even_sum:
       print(f'{i} ',end='')
