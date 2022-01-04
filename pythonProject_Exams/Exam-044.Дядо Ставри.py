days = int(input())

rakia_lit = 0
rakia_g = 0
aver_gr=0

for i in range(days):
    litri = float(input())
    grad = float(input())

    rakia_lit +=litri
    rakia_g += litri*grad
    aver_gr = rakia_g/rakia_lit
    aver_gr_r = round(aver_gr,2)
print(f'Liter: {rakia_lit:.2f}')
print(f'Degrees: {aver_gr_r:.2f}')
if aver_gr < 38:
    print(f'Not good, you should baking!')
elif 38<=aver_gr <= 42:
    print(f'Super!')
elif aver_gr > 42:
    print(f'Dilution with distilled water!')
