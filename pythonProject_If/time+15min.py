hour = int(input())
min = int(input())

time_min = hour * 60 + min + 15

hour = (time_min // 60)
min = time_min % 60

if hour == 24:
    hour = hour - 24
if min < 10:
    print(f'{hour}:0{min}')
else:
    print(f'{hour}:{min}')
