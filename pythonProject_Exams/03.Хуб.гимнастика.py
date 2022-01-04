country = input()
tipe = input()
grade=0
if country == 'Russia':
    if tipe == 'ribbon':
        grade = 9.100+9.400
    elif tipe == 'hoop':
        grade = 9.300+9.800
    elif tipe == 'rope':
        grade = 9.600+9.000
elif country == 'Bulgaria':
    if tipe == 'ribbon':
        grade = 9.600+9.400
    elif tipe == 'hoop':
        grade = 9.550+9.750
    elif tipe == 'rope':
        grade = 9.500+9.400
elif country == 'Italy':
    if tipe == 'ribbon':
        grade = 9.200+9.500
    elif tipe == 'hoop':
        grade = 9.450+9.350
    elif tipe == 'rope':
        grade = 9.700+9.150
diff = 20-grade
pers=diff/20*100
print(f'The team of {country} get {grade:.3f} on {tipe}.')
print(f'{pers:.2f}%')