first_num = int(input())
sec_num = int(input())

for curr_num in range(first_num, sec_num+1):
    odd_digit_sum = 0
    even_digit_sum = 0
    curr_num_as_string = str(curr_num)

    for index, digit in enumerate(curr_num_as_string):
        if index % 2 ==0:
            odd_digit_sum += int(digit)
        else:
            even_digit_sum += int(digit)

    if odd_digit_sum == even_digit_sum:
        print(curr_num, end=' ')
