count_him = int(input())
count_mark = int(input())
prep = float(input())
discount = float(input())

amount_him=count_him*5.80
amount_makt=count_mark*7.20
amount_prep=prep*1.20
sum=amount_makt+amount_him+amount_prep
discount=sum-(sum*discount/100)

print(f'{discount:.3f}')
