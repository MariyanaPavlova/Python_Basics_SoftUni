nailon = int(input())
paint = int(input())
razreditel = int(input())
hours = int(input())

sum_nailon = (nailon + 2) *1.50
sum_paint = (paint + paint*0.10)*14.50
sum_razred = razreditel*5.00

summ = sum_razred+sum_paint+sum_nailon+0.40
rabota = (summ * 0.30) * hours
amount = summ + rabota
print(f'Total expenses: {amount:.2f} lv.')
