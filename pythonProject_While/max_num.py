n = int(input())
counter = 0
max_num = -999999999999999999

while counter < n:
    curr_num = int(input())

    if curr_num > max_num:
        max_num = curr_num
    counter += 1
print(max_num)
