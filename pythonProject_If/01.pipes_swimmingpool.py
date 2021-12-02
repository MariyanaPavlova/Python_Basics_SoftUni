import math
V=int(input())
P1=int(input())
P2=int(input())
time=float(input())

water = (P1+P2)*time
pers_water=math.floor(water/V*100)

tr1=P1*time/water
pers_tr1=math.floor(tr1*100)
tr2=P2*time/water
pers_tr2=math.floor(tr2*100)

prelivane = abs(V-water)
if water<=V:
   print(f'The pool is {pers_water}% full. Pipe 1: {pers_tr1}%. Pipe 2: {pers_tr2}%.')
else:
    print(f'For {time} hours the pool overflows with {prelivane} liters.')