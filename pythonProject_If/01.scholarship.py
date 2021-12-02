import math
dohod=float(input())
aver=float(input())
min_work_payment=float(input())

soc_stip=0
excellent_stip=0

if dohod < min_work_payment and aver > 4.50:
    soc_stip=math.floor(min_work_payment*0.35)

if aver >= 5.50:
    excellent_stip = math.floor(aver * 25)

if soc_stip==0 and excellent_stip==0:
    print(f'You cannot get a scholarship!')
elif soc_stip > excellent_stip:
    print(f'You get a Social scholarship {soc_stip} BGN')
else:
    print(f'You get a scholarship for excellent results {excellent_stip} BGN')

