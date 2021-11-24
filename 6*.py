days = int(input())
cookers = int(input())
cakes = int(input())
gofrets = int(input())
pancakes = int(input())

amount_cakes = cakes * 45
amount_gofrets = gofrets * 5.80
amount_pancakes = pancakes * 3.20

amount_per_day = cookers * (amount_cakes+amount_gofrets+amount_pancakes)
amount_campain = amount_per_day * days
amount_final  = amount_campain - amount_campain/8
print(amount_final)
