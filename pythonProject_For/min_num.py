n = int(input())
min_num = 100000000000000000000000000

for n in range(0,n):
   num = int(input())
   if num < min_num:
       min_num = num
print(min_num)
