name = input()
season = int(input())
ep = int(input())
time = float(input())

add = time*0.20
all_time = time + add
season_additional = season*10
total = season*ep*all_time + season_additional
print(f'Total time needed to watch the {name} series is {round(total)} minutes.')
