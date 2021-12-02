import math
weekends=int(input())

work_days=365-weekends
time_to_play=work_days * 63 + weekends * 127

to_norma=30000-time_to_play
to_norma_a=abs(to_norma)

hours=(to_norma_a//60)
min=to_norma_a%60

if time_to_play > 30000:
    print(f'Tom will run away')
    print(f"{hours} hours and {min} minutes more for play")
else:
    print('Tom sleeps well')
    print(f"{hours} hours and {min} minutes less for play")
