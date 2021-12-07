n = int(input())
max = -100000000000000000000000
min = 9999999999999999999999999

for i in range(n):
    curr_num = int(input())
    if curr_num > max:
        max = curr_num
    if curr_num < min:
        min = curr_num
print(f'Max number: {max}')
print(f'Min number: {min}')
