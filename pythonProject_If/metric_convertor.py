a = float(input())
str1 = str(input()).lower()
str2 = str(input()).lower()

if str1 == 'm':
    out = a
elif str1 == 'mm':
    out = a / 1000
elif str1 == 'cm':
    out = a / 100
if str2 == 'm':
    out = out
elif str2 == 'mm':
    out = out * 1000
elif str2 == 'cm':
    out = out * 100
print(f'{out:.3f}')
