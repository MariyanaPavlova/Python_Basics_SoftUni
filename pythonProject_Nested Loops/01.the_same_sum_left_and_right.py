num1 = int(input())
num2 = int(input())

for i in range (num1, num2+1):
    right_sum = 0
    left_sum = 0
    number = i
    middle_num = 0

    for j in range (1, 6+1):
       curr_num = number % 10
       number //= 10    # маха посл.цифра на number за ясно разбиране
       if j == 1 or j == 2:
           right_sum += curr_num
       elif j == 4 or j == 5:
           left_sum += curr_num
       else:
        middle_num = curr_num

    if left_sum == right_sum:
        print(f'{i} ',end='')
    else:
        if left_sum < right_sum:
            left_sum +=middle_num
        else:
            right_sum +=middle_num
        if left_sum == right_sum:
            print(f'{i} ', end='')



