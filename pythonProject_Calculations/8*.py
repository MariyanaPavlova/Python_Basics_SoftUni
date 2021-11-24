l = int(input())
w = int(input())
h = int(input())
percent = float(input())

v = l * w * h
v_litri = v/1000
percent_fin = percent/100

litters = v_litri - v_litri * percent_fin
print(litters)
