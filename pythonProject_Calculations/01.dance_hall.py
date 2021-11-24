import math
l = float(input())
w = float(input())
a = float(input())

area = l*100*w*100
wardrobe = a*100*a*100
bench=area/10
free_space=area-wardrobe-bench
dancer=40+7000
total=free_space/dancer

print(math.floor(total))