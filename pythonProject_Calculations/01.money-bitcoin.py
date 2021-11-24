count_bitcoin = int(input())
count_yoan = float(input())
commission = float(input())

bitcoin_lv = count_bitcoin * 1168
yoan_to_lv = (count_yoan * 0.15) * 1.76
sum = (bitcoin_lv + yoan_to_lv)/1.95
comm = commission/100 * sum
result = sum - comm
print('%.2f' % result)