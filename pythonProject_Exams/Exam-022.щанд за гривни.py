djobni = float(input())
prodajbi = float(input())
razh = float(input())
price = float(input())

djobni_5 =djobni*5
prodajbi_5 = prodajbi*5
total = djobni_5+prodajbi_5
total_r = total-razh
diff = abs(price - total_r)

if total_r >= price:
    print(f'Profit: {total_r:.2f} BGN, the gift has been purchased.')
else:
    print(f'Insufficient money: {diff:.2f} BGN.')