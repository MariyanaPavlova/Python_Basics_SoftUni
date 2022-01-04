import math
name = input()
epizod = int(input())
lunch_br = int(input())

lunch_time =lunch_br*1/8
free_time = lunch_br*1/4
remain_time = lunch_br-lunch_time-free_time
diff = abs(remain_time-epizod)

if remain_time >= epizod:
    print(f'You have enough time to watch {name} and left with {math.ceil(diff)} minutes free time.')
else:
    print(f"You don't have enough time to watch {name}, you need {math.ceil(diff)} more minutes.")