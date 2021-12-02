v=float(input())
in_m=str(input()).lower()
out_m=str(input()).lower()

if in_m =='m':
    ou=v
elif in_m == 'km':
    ou=v/0.001
elif in_m == 'cm':
    ou=v/100
elif in_m == 'mi':
    ou=v/0.000621371192
elif in_m == 'in':
    ou=v/39.3700787
elif in_m == 'mm':
    ou=v/1000
elif in_m == 'ft':
    ou=v/3.2808399
elif in_m == 'yd':
    ou=v/1.0936133
if out_m == 'ft':
    out=ou*3.2808399
elif out_m == 'in':
    out=ou*39.3700787
elif out_m == 'km':
    out=ou*0.001
elif out_m == 'yd':
    out=ou*1.0936133
elif out_m == 'mi':
    out=ou*0.000621371192
elif out_m == 'cm':
    out=ou*100
elif out_m == 'mm':
    out=ou*1000
elif out_m == 'm':
    out=ou
print(round(out,10))