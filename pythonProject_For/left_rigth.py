n = int(input())
left_sum = 0
right_sum = 0

for i in range (0,n*2):
    curr_sum = int(input())
    if i < n:
        left_sum = left_sum + curr_sum
    elif i >= n:
        right_sum += curr_sum

if left_sum == right_sum:
    print('Yes, sum = '+ str(left_sum))
else:
    diff = abs(left_sum - right_sum)
    print('No, diff = '+str(diff))

#for i in range(0,n):
#curr_sum = int(input())
#left_sum+=curr_sum

#for i in range(0,n):
#curr_sum = int(input())
#right_sum+=curr_sum
