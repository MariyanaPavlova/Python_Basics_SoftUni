trunk = float(input())
luggage = trunk
count_load = 0
load = ''

while luggage >= 0:
    load = input()
    if load == 'End':
        print(f'Congratulations! All suitcases are loaded!')
        break
    load_kg = float(load)

    if count_load % 3 ==0 and count_load != 0:
        load_kg = load_kg+load_kg*0.10
        luggage -= load_kg
    else:
        luggage -= load_kg

    if luggage > 0:
        count_load += 1
    else:
        print(f'No more space!')

print(f"Statistic: {count_load} suitcases loaded.")