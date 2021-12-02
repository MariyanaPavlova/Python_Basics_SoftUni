km=int(input())
day_night=str(input()).lower()

price=0
taxi=0

if day_night =='day':
    taxi=0.79
else:
    taxi=0.90

if km<20:
    price=0.70+km*taxi
elif km<100:
    price=km*0.09
else:
    price=km*0.06
print(price)