l = int(input())
w = int(input())
h = int(input())
pers=float(input())
v=l*w*h
v_l=v/1000
persentige = pers/100
needed_l = v_l * (1-persentige)
print(f'{needed_l:.3f}')