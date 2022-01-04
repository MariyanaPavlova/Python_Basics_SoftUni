count = int(input())

back=0
chest=0
legs=0
abss=0
prot_shake=0
prot_bar=0

for i in range(count):
    tipe = input()

    if tipe == 'Back':
        back +=1
    elif tipe == 'Chest':
        chest +=1
    elif tipe == 'Legs':
        legs +=1
    elif tipe == 'Abs':
        abss +=1
    elif tipe == "Protein shake":
        prot_shake +=1
    elif tipe == 'Protein bar':
        prot_bar +=1
aver = (back+chest+legs+abss)/count*100
prod = (prot_shake+prot_bar)/count*100
print(f'{back} - back')
print(f'{chest} - chest')
print(f'{legs} - legs')
print(f'{abss} - abs')
print(f'{prot_shake} - protein shake')
print(f'{prot_bar} - protein bar')
print(f'{aver:.2f}% - work out')
print(f'{prod:.2f}% - protein')


