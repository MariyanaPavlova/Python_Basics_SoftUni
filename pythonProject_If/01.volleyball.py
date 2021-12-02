import math
year = input().lower()
holidays = int(input())
weekends_home = int(input())
add = 0
play_total = 0

sofia_weekends = (48 - weekends_home) * 3 / 4 + (holidays * 2 / 3) + weekends_home

if year == 'leap':
    add = sofia_weekends * 0.15
    play_total = sofia_weekends + add
elif year == 'normal':
    play_total = sofia_weekends

print(math.floor(play_total))
