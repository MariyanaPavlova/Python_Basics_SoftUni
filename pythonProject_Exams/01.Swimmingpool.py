import math
people = int(input())
entrance = float(input())
shejlong = float(input())
umbrela = float(input())

entrance_tax = entrance*people
shejlong_tax = math.ceil(people*0.75)*shejlong
umbrela_tax = math.ceil(people*0.5)*umbrela
sum = entrance_tax+shejlong_tax+umbrela_tax
print(f'{sum:.2f} lv.')
