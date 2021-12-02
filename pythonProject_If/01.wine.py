import math
loze=int(input())
Y=float(input())
Z=int(input())
rabot=int(input())

grozde_1 = 1*Y
rekolta = loze*grozde_1
pers = rekolta*0.40
vino = pers/2.5
diff = abs(Z - vino)
za_rabot=diff/rabot

if vino >= Z:
    print(f'Good harvest this year! Total wine: {math.floor(vino)} liters.')
    print(f"{math.ceil(diff)} liters left -> {math.ceil(za_rabot)} liters per person.")
else:
    print(f"It will be a tough winter! More {math.floor(diff)} liters wine needed.")