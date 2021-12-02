flowers = input()
count_flowers = int(input())
budget = int(input())

roses = 5
dahlias = 3.80
tulips = 2.80
narcissus = 3
grladiolus = 2.50

price = 0

if flowers == 'Roses':
    price = count_flowers * roses
elif flowers == 'Dahlias':
    price = count_flowers * dahlias
elif flowers == 'Tulips':
    price = count_flowers * tulips
elif flowers == 'Narcissus':
    price = count_flowers * narcissus
elif flowers == 'Gladiolus':
    price = count_flowers * grladiolus

if flowers == 'Roses' and count_flowers > 80:
    price = count_flowers * roses - (count_flowers * roses * 0.10)
elif flowers == 'Dahlias' and count_flowers > 90:
    price = count_flowers * dahlias - (count_flowers * dahlias * 0.15)
elif flowers == 'Tulips' and count_flowers > 80:
    price = count_flowers * tulips - (count_flowers * tulips * 0.15)
elif flowers == 'Narcissus' and count_flowers < 120:
    price = count_flowers * narcissus + (count_flowers * narcissus * 0.15)
elif flowers == 'Gladiolus' and count_flowers < 80:
    price = count_flowers * grladiolus + (count_flowers * grladiolus * 0.20)

remaining = budget - price
remaining_abs = abs(remaining)

if budget >= price:
    print(f'Hey, you have a great garden with {count_flowers} {flowers} and {remaining_abs:.2f} leva left.')
else:
    print (f"Not enough money, you need {remaining_abs:.2f} leva more.")