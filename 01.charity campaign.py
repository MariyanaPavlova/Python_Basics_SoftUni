dni=int(input())
sladkari=int(input())
torti=int(input())
gofreti=int(input())
palachinki=int(input())

torti_sum=torti * 45
gofreti_sum=gofreti*5.80
palachinki_sum=palachinki*3.20

total_sladki=(torti_sum+gofreti_sum+palachinki_sum)*sladkari*dni
#print(total_sladki)
edna_osma=total_sladki/8
#print(edna_osma)
total=total_sladki-edna_osma
print(f'{total:.2f}')
