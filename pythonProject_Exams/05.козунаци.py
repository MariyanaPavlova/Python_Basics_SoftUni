import math
count = int(input())

sugarr = 0
flourr =0
max_sugar=0
max_flour=0
for i in range(count):
    sugar = int(input())
    flour = int(input())
    sugarr += sugar
    flourr += flour
    if sugar>max_sugar:
        max_sugar=sugar
    if flour>max_flour:
        max_flour=flour

packets_sugar = math.ceil(sugarr/950)
packets_flour = math.ceil(flourr/750)

print(f'Sugar: {packets_sugar}')
print(f'Flour: {packets_flour}')
print(f'Max used flour is {max_flour} grams, max used sugar is {max_sugar } grams.')
