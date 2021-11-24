count_tables = int(input())
l_tables=float(input())
w_tables=float(input())

pokrivki = count_tables *((l_tables +2*0.30)*(w_tables+2*0.3))
kare = count_tables * ((l_tables/2)*(l_tables/2))

usd=pokrivki*7+kare*9
print(f'{usd:.2f} USD')
bgn=usd*1.85
print(f'{bgn:.2f} BGN')