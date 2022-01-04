bitcoin = int(input())
yoan = float(input())
comm = float(input())

bitcoin_amount = bitcoin * 1168
yoan_amount = (yoan * 0.15) * 1.76
amount = (bitcoin_amount + yoan_amount)/1.95
commision = amount * comm/100
result = amount - commision

print(f'{result:.2f}')
