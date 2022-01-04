count = int(input())
eggs = int(input())
kg = int(input())

kozun = count * 3.20
kori = eggs * 4.35
kur = kg * 5.40
boia = eggs * 12 *0.15
total = kozun + kori + kur + boia
print(f'{total:.2f}')
