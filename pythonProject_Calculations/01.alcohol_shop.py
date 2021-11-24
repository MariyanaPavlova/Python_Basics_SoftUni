price_wiskey=float(input())
l_beer=float(input())
l_wine=float(input())
l_rakia=float(input())
l_wiskey=float(input())

price_rakia=price_wiskey/2
price_wine=price_rakia-price_rakia*0.40
price_beer=price_rakia-price_rakia*0.80

sum_rakia=l_rakia*price_rakia
sum_wine=l_wine*price_wine
sum_beer=l_beer*price_beer
sum_wiskey=l_wiskey*price_wiskey
sum=sum_rakia+sum_wine+sum_beer+sum_wiskey
print(f'{sum:.2f}')