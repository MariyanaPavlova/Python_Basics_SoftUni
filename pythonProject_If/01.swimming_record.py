import math

record = float(input())
distance = float(input())
time_1m = float(input())

ivan = distance * time_1m
delay = math.floor(distance / 15) * 12.5
total = ivan + delay
slower = abs(record - total)
if record > total:
    print(f'Yes, he succeeded! The new world record is {total:.2f} seconds.')
else:
    print(f'No, he failed! He was {slower:.2f} seconds slower.')
