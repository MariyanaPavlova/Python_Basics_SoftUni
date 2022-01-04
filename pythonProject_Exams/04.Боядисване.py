h = int(input())
w = int(input())
percent = int(input())
liters = input()

wall = h * w * 4
wall_wind = wall - wall*percent/100
wall_wind_paint = wall_wind

while liters != 'Tired!':
    liters_i = int(liters)

    wall_wind_paint -= liters_i
    liters_tot += liters_i

    if wall_wind_paint < 0:
        print(f"All walls are painted and you have {abs(round(wall_wind_paint))} l paint left!")
        break
    elif wall_wind_paint == 0:
        print("All walls are painted! Great job, Pesho!")
        break
    liters = input()

else:
    print(f'{round(wall_wind_paint)} quadratic m left.')
